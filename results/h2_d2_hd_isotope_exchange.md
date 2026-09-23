# Isotope-exchange thermochemistry: H₂ + D₂ → 2 HD

| Setting | Value |
| --- | --- |
| Electronic method | B3LYP/6-31G(d) |
| Temperature | 298.15 K |
| Pressure | 1 bar |
| Execution | PySCF on Slurm, 1 CPU core |
| Thermochemical model | Ideal-gas classical RRHO |
| Nuclear-spin statistics | Omitted |

## Result

**ΔG = −2.919163 kJ/mol**

This is −0.001111850577474982 Hartree for the reaction H₂ + D₂ → 2 HD.

The optimized H–H bond length was 0.742788 Å. The harmonic frequencies used
for H₂, D₂, and HD were 4453.13, 3150.05, and 3857.02 cm⁻¹, respectively.

MAESTRO does not currently provide a task that propagates isotopic masses
through vibrational, rotational, and translational thermochemistry to a
reaction free energy. The calculation therefore uses the included raw PySCF
script and explicit isotope-resolved RRHO post-processing.

See the [machine-readable result](../h2_d2_hd_thermo_work/h2_d2_hd_result.json),
[calculation script](../h2_d2_hd_thermo_work/h2_d2_hd_delta_g.py), and
[Slurm submission script](../h2_d2_hd_thermo_work/submit.slurm).
