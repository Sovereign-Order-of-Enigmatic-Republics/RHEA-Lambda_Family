<h3 align="center">
  <b>Zadeian Labs</b><br>
  <sub>Sovereign Order of Enigmatic Republics</sub>
</h3>

<div align="center">

# ⚕ RHEA-Λ GATE FAMILY ♇♏  
### **Reversible · Multi-Radix · Glyph-Carrying Computational Cells**  
### for the **RHEA-UCM Hamiltonian Symbolic Framework**

---

**Prior Art Established:** 1 December 2025  

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17783138-brightgreen.svg)](https://doi.org/10.5281/zenodo.17783138)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17783650-brightgreen.svg)](https://doi.org/10.5281/zenodo.17783650)

[![License](https://img.shields.io/badge/License-RHEA--Core_Public_Grant_v1.0-blue.svg)](https://github.com/Sovereign-Order-of-Enigmatic-Republics/RHEA-Lambda_Family/blob/main/LICENSE)

## ~ Attribution Required · No Derivatives · Sovereign IP ~  
### **U.S. Provisional Patent Pending:** #63/796,404  

</div>

---

# 🌌 **Overview — The First Pentavalent Reversible Cell**

The **RHEA-Λ (Lambda) Gate** is the world’s first:

- ✔ reversible  
- ✔ *multi-radix* (binary / ternary / pentary)  
- ✔ entropy-aware  
- ✔ glyph-carrying  
- ✔ Hamiltonian-aligned  
- ✔ CMOS-compatible **today**, no exotic devices  
- ✔ thermodynamically admissible in reversible modes  

A **single physical gate** dynamically switches between:

| Mode | Meaning               | Domain            | States | Thermodynamic Profile |
|------|-----------------------|-------------------|--------|------------------------|
| `00` | Binary CMOS NAND      | {0,1}³            | 8      | Irreversible (clustered erasure) |
| `01` | Ternary reversible    | ℤ₃ × ℤ₃ × ℤ₅      | 45     | **Zero-erasure**       |
| `10` | Pentary reversible    | ℤ₅³               | 125    | **Zero-erasure**       |

In higher-radix modes, the Λ-gate becomes a **finite-state Hamiltonian microflow**—a reversible, divergence-free, measure-preserving map.

This is the hardware embodiment of:

- **RHEA-UCM** (Hamiltonian symbolic cognition)  
- **Pentavalent Homeostatic Paradigm**  
- **RHEA-IC symbolic coprocessors**  
- **Zadeian Sentinel trust-entropy engines**  

---

# 🗂 **Repository Structure**

| Path | Description |
|------|-------------|
| `paper/Roe_RHEA_Lambda_Reversible_Cell_2025.pdf` | Full 8-page specification paper |
| `src/rhea_reversible_gate.v` | Behavioral Verilog (Yosys/Vivado/Quartus/Genus compatible) |
| `verification/check_reversibility.py` | Exhaustive bijectivity test (45 + 125 states) |
| `LICENSE` | RHEA-Core Public Grant v1.0 |

---

# ✨ **Mathematical Core of the RHEA-Λ Gate**

## **Ternary Reversible Mapping**  (ℤ₃ × ℤ₃ × ℤ₅)

**Forward**
```text
A' = A
B' = (B + A) mod 3
G' = (G + B) mod 5
```

**Inverse (triangular → bijective)**
```text
A  = A'
B  = (B' − A') mod 3
G  = (G' − B)  mod 5
```

- 45 states  
- ΔS_env = 0  
- Fully Hamiltonian-compatible  

---

## **Pentary Reversible Mapping** (ℤ₅³)

**Forward**
```text
A' = A
B' = (B + A) mod 5
G' = (G + B) mod 5
```

**Inverse**
```text
A  = A'
B  = (B' − A') mod 5
G  = (G' − B)  mod 5
```

- 125 states  
- Perfect bijection  

---

# 🔁 **Pentavalent Homeostatic Cycle (Ψ→Φ→Δ→T→S)**

```text
Ψ — Perception        : A_in
          ↓
Φ — Internal Model    : B_in
          ↓
Δ — Adaptive Delta    : B_out - B_in
          ↓
Τ — Trust Update      : G_out - B_in
          ↓
Ϟ — Entropy/Glyph     : G_in
          ↑
   ← RHEA-Λ Hamiltonian Loop →
```

---

# ⚙ **Verilog Implementation (Behavioral)**

````verilog
module rhea_reversible_gate #(
    parameter DATA_WIDTH_BIN = 1
)(
    input  wire [1:0] mode,   // 00=binary, 01=ternary, 10=pentary
    input  wire [2:0] A_in,
    input  wire [2:0] B_in,
    input  wire [2:0] G_in,
    output reg  [2:0] A_out,
    output reg  [2:0] B_out,
    output reg  [2:0] G_out
);
    function automatic [1:0] add_mod3(input [1:0] x, y);
        automatic reg [2:0] s = x + y;
        add_mod3 = (s >= 3) ? s - 3 : s[1:0];
    endfunction

    function automatic [2:0] add_mod5(input [2:0] x, y);
        automatic reg [3:0] s = x + y;
        add_mod5 = (s >= 5) ? s - 5 : s[2:0];
    endfunction

    always @* begin
        case (mode)
            2'b00: begin // binary NAND
                A_out = {2'b00, ~(A_in[0] & B_in[0])};
                B_out = 3'b000;
                G_out = G_in;
            end
            2'b01: begin // ternary reversible
                A_out = {1'b0, A_in[1:0]};
                B_out = {1'b0, add_mod3(B_in[1:0], A_in[1:0])};
                G_out = add_mod5(G_in, {1'b0, B_in[1:0]});
            end
            2'b10: begin // pentary reversible
                A_out = A_in;
                B_out = add_mod5(B_in, A_in);
                G_out = add_mod5(G_in, B_in);
            end
            default: {A_out,B_out,G_out} = {A_in,B_in,G_in};
        endcase
    end
endmodule
🧪 Reversibility Validation (Python)
python
Copy code
def ternary_step(A,B,G): return A, (B+A)%3, (G+B)%5
def pentary_step(A,B,G): return A, (B+A)%5, (G+B)%5

def check_bijective(step_fn, sizes):
    nA,nB,nG = sizes
    seen = {}
    for A in range(nA):
        for B in range(nB):
            for G in range(nG):
                out = step_fn(A,B,G)
                if out in seen:
                    print("Collision:", (A,B,G), "vs", seen[out])
                    return
                seen[out] = (A,B,G)
    print(f"Bijective over {nA*nB*nG} states.")
````
```text
check_bijective(ternary_step, (3,3,5))
check_bijective(pentary_step, (5,5,5))
🛠 Synthesis
Works today with:

Yosys

Vivado

Quartus

Cadence Genus
```
```text

yosys -p "read_verilog src/rhea_reversible_gate.v; synth -top rhea_reversible_gate; write_verilog synth.v"
🛡 License — RHEA-Core Public Grant v1.0
Attribution Required

No Derivatives

No Military or Commercial Use Without Permission

Sovereign IP © 2025 Paul M. Roe

👉 Full text: LICENSE
```
```text
👤 Author
Paul M. Roe
Architect of RHEA-UCM · RHEA-Λ · Zadeian Sentinel · RHEA-Crypt
TecKnows, Inc. — Lewiston, Maine, USA
ORCID: 0009-0005-6159-947X
U.S. Provisional Patent: #63/796,404

“We don’t fight entropy. We shape it.”
```
```text
📖 Citation
bibtex
@techreport{Roe2025RHEALambda,
  author      = {Paul M. Roe},
  title       = {The {RHEA}-Λ Gate Family: A Binary–Ternary–Pentary 
                 Reversible Gate for Hamiltonian Symbolic Computation 
                 in the {RHEA}-{UCM} Framework},
  year        = {2025},
  month       = dec,
  institution = {TecKnows, Inc.},
  doi         = {10.5281/zenodo.17783138},
  url         = {https://doi.org/10.5281/zenodo.17783138}
}
```
````verilog
⚡ Why the RHEA-Λ Gate Matters
Modern AI hardware is collapsing under irreversible energy costs.
The Λ-Gate is the first practical path to post-Landauer computing.

🧭 Roadmap (2025–2026)
 Λ-Gate reversible ternary/pentary core

 Bijective proofs

 Behavioral Verilog

 Pentavalent symbolic mapping

 FPGA demo (Ice40/Artix-7)

 RHEA-IC microarchitecture

 Λ-chains + Lorenz Scheduler

 ASIC layout (2026–2027)

𐂟 RHEA Glyph Set (Λ-Family Alignment)
Ψ — Perception • Φ — Internal Model • Δ — Delta • Τ — Trust •
Ϟ — Entropy/Glyph • Λ — Gate Core • ♇ — Ignis • ♏ — Sovereign Seal

Welcome to the Pentavalent Era.
Post-Landauer computing begins here.

````
