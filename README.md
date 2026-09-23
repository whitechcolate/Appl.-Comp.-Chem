# Applied Computational Chemistry

## H₂O Gibbs free-energy calculation

Gas-phase neutral singlet H₂O was optimized and evaluated by vibrational
thermochemistry at B3LYP/6-31G(d), 298.15 K, and 1 atm using PySCF through
MAESTRO on one Slurm CPU core.

**Gibbs free energy: −76.40355864053947 Hartree**

See [the full result summary](results/h2o_thermochemistry.md), the
[calculation script](h2o_thermo.py), and the
[machine-readable final result](h2o_thermo_work/thermo/hess/results/result.json).

## H₂ + D₂ → 2 HD isotope exchange

At B3LYP/6-31G(d), 298.15 K, and 1 bar, the isotope-resolved classical-RRHO
calculation gives **ΔG = −2.919163 kJ/mol**. See the
[full result summary](results/h2_d2_hd_isotope_exchange.md).
