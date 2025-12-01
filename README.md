# RHEA-Reversible-Cell  
**The world’s first reversible, multi-radix, glyph-carrying computational primitive**  
**Prior art established: 1 December 2025**  
**License:** RHEA-Core Public Grant v1.0 (see [LICENSE](LICENSE))

[![Prior Art](https://img.shields.io/badge/Prior_Art-Established_1_Dec_2025-red.svg)](https://github.com/Sovereign-Order-of-Enigmatic-Republics/RHEA-Reversible-Cell)  
[![License](https://img.shields.io/badge/License-RHEA--Core_Public_Grant_v1.0-blue.svg)](LICENSE)  
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.xxxxxxx-brightgreen.svg)](https://doi.org/10.5281/zenodo.xxxxxxx) ← (add after Zenodo upload)

### A single CMOS-compatible gate that dynamically switches between  
- **Binary** (standard irreversible NAND – full legacy compatibility)  
- **Ternary** reversible mode over ℤ₃×ℤ₃×ℤ₅ (45 states)  
- **Pentary** reversible mode over ℤ₅³ (125 states)  

All higher-radix modes are **strictly bijective** → zero information erasure → thermodynamically admissible symbolic computation.

This cell is the hardware-level incarnation of the **Pentavalent Homeostatic Paradigm** and the **RHEA-UCM Hamiltonian symbolic framework** (three papers currently in review at SIAM journals).

## Files

| File / Folder                     | Description                                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------------------|
| `paper/RHEA_Reversible_Cell_Roe_2025.pdf` | Full specification paper (8 pages, LaTeX source available on request)              |
| `src/rhea_reversible_gate.v`      | Synthesizable behavioral Verilog (Yosys, Vivado, Quartus, Genus compatible)        |
| `verification/check_reversibility.py` | Exhaustive bijectivity proof for ternary & pentary modes (45 & 125 states)        |
| `LICENSE`                         | RHEA-Core Public Grant v1.0 – revocable, non-commercial, non-sublicensable, attribution-required |

## Quick Start – Verify Reversibility

```bash
cd verification
python3 check_reversibility.py
Expected output:
text=== Checking Ternary (ℤ₃ × ℤ₃ × ℤ₅) mode ===
State space: 3 × 3 × 5 = 45 states
Mapping is bijective over 45 states.

=== Checking Pentary (ℤ₅³) mode ===
State space: 5 × 5 × 5 = 125 states
Mapping is bijective over 125 states.

All reversible modes are mathematically proven bijective.
Zero-erasure symbolic computation is thermodynamically admissible.
Synthesis (example with Yosys)
Bashyosys -p "read_verilog src/rhea_reversible_gate.v; synth -top rhea_reversible_gate; write_verilog synth.v"
The gate uses only standard-cell combinational logic + tiny 3-bit registers for the glyph/entropy state G – no exotic devices, no adiabatic resonators, no new PDK required.
Mapping to the Pentavalent Homeostatic Cycle (Ψ→Φ→Δ→T→S)






Pentavalent PhaseGate SignalRoleΨ (Perception)A_inPrimary symbolic operand (unchanged)Φ (Internal model)B_inSecondary operandΔ (Adaptive delta)B_out - B_inModular kick from AT (Trust)G_out - B_inPhase/trust incrementS (Entropy state)GLocal glyph/entropy accumulator
Author
Paul M. Roe
TecKnows, Inc. – Lewiston, Maine, USA
ORCID: 0009-0005-6159-947X
U.S. Provisional Patent Pending 63/796,404
Copyright © 2025 Paul M. Roe – All Rights Reserved
RHEA-UCM© · RHEA-Crypt© · Pentavalent Homeostatic Paradigm©
Citation
textRoe, P. M. (2025). A Reversible Multi-Radix Computational Cell for Hamiltonian Symbolic Processing 
in the RHEA-UCM Framework. https://doi.org/10.5281/zenodo.xxxxxxx
The future of post-Landauer computing just became open hardware.
Welcome to the Pentavalent era.
