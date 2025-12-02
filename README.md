RHEA-Λ Gate Family
Reversible, Multi-Radix, Glyph-Carrying Computational Cells for the RHEA-UCM Framework

Prior Art Established: 1 December 2025
License: RHEA-Core Public Grant v1.0








Overview

The RHEA-Λ Gate Family is the world's first open, reversible, multi-radix computational primitive designed to support the Pentavalent Homeostatic Paradigm and the Hamiltonian symbolic structure of the RHEA-UCM framework.

Each RHEA-Λ cell provides:

Binary mode — Standard CMOS-compatible irreversible NAND (full backwards compatibility).

Ternary reversible mode over ℤ₃ × ℤ₃ × ℤ₅ (45-state Hamiltonian microcell).

Pentary reversible mode over ℤ₅³ (125-state Hamiltonian microcell).

A 3-bit glyph/entropy register (G) — enabling symbolic memory, trust state, and entropy flow.

High-radix modes are fully bijective, providing zero-erasure symbolic computation compatible with:

Landauer/Bennett limits

Divergence-free Hamiltonian flows

Measure-preserving symbolic recursion (RHEA-UCM)

The RHEA-Λ family forms the foundational hardware-level substrate for future RHEA-IC processors, RHEA-Crypt accelerators, agentic substrates, and reversible symbolic AI.

Key Features
🔹 Three logical faces, one physical gate
Mode	Domain	Behavior
00	Binary	Drop-in CMOS irreversible NAND
01	Ternary	Bijective over ℤ₃×ℤ₃×ℤ₅
10	Pentary	Bijective over ℤ₅³

All transformations are triangular and perfectly invertible:

No collisions

No erasures

No entropy production

Exactly as required by Hamiltonian computation.

Repository Structure
Path	Description
paper/RHEA_Reversible_Cell_Roe_2025.pdf	Full academic paper (LaTeX-ready)
src/rhea_reversible_gate.v	Behavioral Verilog (Yosys / Vivado / Quartus compatible)
verification/check_reversibility.py	Enumerates 45 and 125-state spaces for bijectivity proof
LICENSE	RHEA-Core Public Grant v1.0
Quick Verification (Bijectivity Proof)
cd verification
python3 check_reversibility.py


You should see:

=== Checking Ternary (ℤ₃ × ℤ₃ × ℤ₅) mode ===
State space: 45
Mapping is bijective.

=== Checking Pentary (ℤ₅³) mode ===
State space: 125
Mapping is bijective.

All reversible modes validated.

Synthesis Example (Yosys)
yosys -p "read_verilog src/rhea_reversible_gate.v; synth -top rhea_reversible_gate; write_verilog synth.v"


No exotic PDKs. No adiabatic resonators. No cryogenic CMOS.
Just standard combinational logic + a 3-bit register.

Pentavalent Homeostatic Cycle (Ψ → Φ → Δ → T → S)
Phase	Gate Signal	Role
Ψ	A_in	Input operand
Φ	B_in	Secondary operand / local model
Δ	B_out − B_in	Adaptive delta
T	G_out − B_in	Trust transfer / phase modulation
S	G_in	Local entropy/glyph accumulator

This matches the Pentavalent Paradigm and integrates directly with RHEA-UCM Hamiltonian operators.

Citation
Roe, P. M. (2025).
A Reversible Multi-Radix Computational Cell for Hamiltonian Symbolic Processing
in the RHEA-UCM Framework.
Zenodo. DOI: 10.5281/zenodo.17783138

Author

Paul M. Roe
TecKnows, Inc. — Lewiston, Maine, USA
ORCID: 0009-0005-6159-947X
U.S. Provisional Patent Pending #63/796,404
Copyright © 2025

“The future of post-Landauer computing just became open hardware.”

Welcome to the Pentavalent Era.
