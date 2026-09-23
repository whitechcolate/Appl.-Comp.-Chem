---
task: unsupported
engine: none
error_class: support_gap
outcome: support_gap
---
Symptom: Requested the Gibbs free energy of H2 + D2 -> 2 HD with isotope-resolved translational, rotational, and vibrational thermochemistry.
Attempts: Searched MAESTRO capabilities for reaction, thermochemistry, isotope, and Gibbs terms. IsotopeShiftTask provides isotope-shifted harmonic frequencies; ThermoReevalTask accepts frequencies and a geometry but derives translational and rotational masses from elemental symbols, so it cannot represent D/H isotopologues fully. ReactionProfileTask expects a reaction path and precomputed Gibbs energies.
Result: No MAESTRO task combines isotope masses with complete thermochemistry and reaction stoichiometry.
Context: A dedicated isotope-resolved thermochemistry/reaction-free-energy task is missing.
