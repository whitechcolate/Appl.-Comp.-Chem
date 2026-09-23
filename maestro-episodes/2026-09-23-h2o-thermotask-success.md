---
task: ThermoTask
engine: pyscf
error_class: none
outcome: success
wall_time_s: 19
n_atoms: 3
method: B3LYP
basis: 6-31G(d)
cores: 1
mode: slurm
---
Symptom: None. The optimization and Hessian nodes both completed with converged SCF indicators.
Attempts: The approved Slurm submission was retried once with cluster access after the sandbox could not contact the Slurm controller. The submitted PySCF jobs then completed on their first engine attempt.
Result: Gibbs free energy at 298.15 K and 1 atm was -76.40355864053947 Hartree.
Context: Isolated neutral singlet H2O, gas phase, B3LYP/6-31G(d), one CPU core. Measured engine wall times were 10 s for optimization and 9 s for the Hessian.
