---
task: unsupported
engine: pyscf
error_class: none
outcome: workaround
n_atoms: 2
method: B3LYP
basis: 6-31G(d)
cores: 1
mode: slurm
---
Symptom: MAESTRO lacks a task that carries isotope masses through vibrational, rotational, and translational thermochemistry to a reaction Gibbs free energy.
Attempts: Ran a raw PySCF B3LYP/6-31G(d) H2 optimization and Hessian on one Slurm CPU. Applied isotope-specific classical RRHO partition functions to H2, D2, and HD. The first raw job had a Slurm working-directory setup failure; a corrected resubmission completed. A frequency-conversion error found during output validation was corrected before the final resubmission.
Result: At 298.15 K and 1 bar, ΔG for H2 + D2 -> 2 HD is -0.001111850577474982 Hartree (-2.9191632903160842 kJ/mol). Nuclear-spin statistical weights were omitted.
Context: The final harmonic frequencies were 4453.13 cm^-1 (H2), 3150.05 cm^-1 (D2), and 3857.02 cm^-1 (HD). Slurm accounting was disabled, so measured wall time was unavailable.
