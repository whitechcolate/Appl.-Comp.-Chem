"""Classical-RRHO isotope-exchange free energy: H2 + D2 -> 2 HD.

The B3LYP/6-31G(d) Born-Oppenheimer surface and Hessian are evaluated once
for H2. Isotopologue-specific masses are then used for harmonic vibrational,
rotational, and translational partition functions at 298.15 K and 1 bar.
Nuclear-spin statistical weights are not included, matching conventional
electronic-structure thermochemistry output.
"""

import json
import math
from pathlib import Path

import numpy as np
from pyscf import dft, gto
from pyscf.geomopt.geometric_solver import optimize

T = 298.15
P_BAR = 1.0
HARTREE_J = 4.3597447222071e-18
KB_J_K = 1.380649e-23
H_J_S = 6.62607015e-34
C_CM_S = 2.99792458e10
AMU_KG = 1.66053906660e-27
AMU_TO_ME = 1822.888486209
HARTREE_PER_CM = H_J_S * C_CM_S / HARTREE_J
R_HARTREE_K = KB_J_K / HARTREE_J
HARTREE_TO_KJMOL = 2625.4996394799

# Isotopic atomic masses in u.
MASS_H = 1.00782503223
MASS_D = 2.01410177812


def rrho_gibbs(electronic_energy, hessian, coords_angstrom, masses_amu, sigma):
    """Ideal-gas linear-molecule RRHO Gibbs free energy in Hartree."""
    nat = len(masses_amu)
    # PySCF orders Hessian axes as (atom_i, atom_j, cart_i, cart_j).
    # Reorder to the conventional (atom_i, cart_i, atom_j, cart_j)
    # matrix before mass weighting.
    mw_hessian = hessian.transpose(0, 2, 1, 3).reshape(3 * nat, 3 * nat).copy()
    mass_me = np.repeat(np.asarray(masses_amu) * AMU_TO_ME, 3)
    mw_hessian /= np.sqrt(np.outer(mass_me, mass_me))
    eigvals = np.linalg.eigvalsh(mw_hessian)
    # A diatomic has one vibrational degree of freedom; retain the stretch.
    omega_au = math.sqrt(max(float(eigvals[-1]), 0.0))
    # In atomic units the Hessian eigenvalue gives angular frequency and
    # E = hbar*omega, so Eh/(h*c) converts it directly to cm^-1.
    frequency_cm = omega_au * 219474.63136320

    zpe = 0.5 * frequency_cm * HARTREE_PER_CM
    x = H_J_S * C_CM_S * frequency_cm / (KB_J_K * T)
    e_vib = frequency_cm * HARTREE_PER_CM / math.expm1(x)
    s_vib = R_HARTREE_K * (x / math.expm1(x) - math.log1p(-math.exp(-x)))

    mass_kg = float(sum(masses_amu)) * AMU_KG
    volume = KB_J_K * T / (P_BAR * 1.0e5)
    lam = 2.0 * math.pi * mass_kg * KB_J_K * T / H_J_S**2
    s_trans = R_HARTREE_K * (math.log(lam**1.5 * volume) + 2.5)

    xyz_m = np.asarray(coords_angstrom) * 1.0e-10
    masses_kg = np.asarray(masses_amu) * AMU_KG
    com = np.average(xyz_m, axis=0, weights=masses_kg)
    rel = xyz_m - com
    inertia = float(np.sum(masses_kg * np.sum(rel * rel, axis=1)))
    q_rot = 8.0 * math.pi**2 * inertia * KB_J_K * T / (sigma * H_J_S**2)
    s_rot = R_HARTREE_K * (math.log(q_rot) + 1.0)

    h_correction = zpe + e_vib + 3.5 * R_HARTREE_K * T
    gibbs = electronic_energy + h_correction - T * (s_trans + s_rot + s_vib)
    return {
        "gibbs_hartree": gibbs,
        "frequency_cm-1": frequency_cm,
        "zpe_hartree": zpe,
        "entropy_hartree_per_k": s_trans + s_rot + s_vib,
    }


def run():
    initial = gto.M(
        atom="H 0 0 -0.37; H 0 0 0.37",
        basis="6-31g(d)",
        unit="Angstrom",
        charge=0,
        spin=0,
        verbose=4,
    )
    initial_mf = dft.RKS(initial)
    initial_mf.xc = "B3LYP"
    initial_mf.grids.level = 3
    initial_mf.kernel()
    optimized = optimize(initial_mf, maxsteps=50)

    mf = dft.RKS(optimized)
    mf.xc = "B3LYP"
    mf.grids.level = 3
    electronic_energy = mf.kernel()
    hessian = mf.Hessian().kernel()
    coords = optimized.atom_coords(unit="Angstrom")

    results = {
        "H2": rrho_gibbs(electronic_energy, hessian, coords, (MASS_H, MASS_H), 2),
        "D2": rrho_gibbs(electronic_energy, hessian, coords, (MASS_D, MASS_D), 2),
        "HD": rrho_gibbs(electronic_energy, hessian, coords, (MASS_H, MASS_D), 1),
    }
    delta_g = 2.0 * results["HD"]["gibbs_hartree"] - results["H2"]["gibbs_hartree"] - results["D2"]["gibbs_hartree"]
    payload = {
        "reaction": "H2 + D2 -> 2 HD",
        "method": "B3LYP/6-31G(d)",
        "temperature_K": T,
        "pressure_bar": P_BAR,
        "model": "ideal-gas classical RRHO; nuclear-spin statistical weights omitted",
        "optimized_h2_bond_length_angstrom": float(np.linalg.norm(coords[1] - coords[0])),
        "electronic_energy_hartree": electronic_energy,
        "species": results,
        "delta_g_hartree": delta_g,
        "delta_g_kj_mol": delta_g * HARTREE_TO_KJMOL,
    }
    Path("h2_d2_hd_result.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    run()
