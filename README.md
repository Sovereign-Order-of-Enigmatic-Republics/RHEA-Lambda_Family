⚕🜂 RHEA-Λ GATE FAMILY ♇♏
Reversible · Multi-Radix · Glyph-Carrying Computational Cells
for the RHEA-UCM Hamiltonian Symbolic Framework
<div align="center">








</div>
🜂 Overview — The First Pentavalent Reversible Cell

The RHEA-Λ (Lambda) Gate is the world’s first:

reversible

multi-radix (₂ / ₃ / ₅-ary)

entropy-aware

glyph-carrying

Hamiltonian-aligned

CMOS-compatible

computational primitive.

A single physical gate dynamically switches between:

Mode	Meaning	Domain	Thermodynamic Profile
00	Binary CMOS NAND	0/1	Irreversible, erasure-clustered
01	Ternary reversible	ℤ₃ × ℤ₃ × ℤ₅ (45 states)	Zero-erasure
10	Pentary reversible	ℤ₅³ (125 states)	Zero-erasure

In higher-radix modes, the Λ-gate becomes a finite-state Hamiltonian microflow—perfectly bijective, divergence-free, and entropy-neutral.

This is the hardware embodiment of:

⚕ RHEA-UCM
🜂 Pentavalent Homeostatic Paradigm
♇ RHEA-IC symbolic processors
♛ Zadeian Sentinel trust-entropy computation

⚛ Repository Structure
Path	Description
paper/Roe_RHEA_Lambda_Reversible_Cell_2025.pdf	Full specification paper (8 pages)
src/rhea_reversible_gate.v	Behavioral Verilog implementation
verification/check_reversibility.py	Exhaustive reversibility validation
LICENSE	RHEA-Core Public Grant v1.0 — Attribution Required, No Derivatives
🜂 Mathematical Core of the RHEA-Λ Gate
Binary Mode (CMOS NAND)

Used for compatibility + controllable entropy discharge.

A_out = NAND(A, B)
B_out = 0
G_out = G

Ternary Reversible Mapping (ℤ₃ × ℤ₃ × ℤ₅)

For A, B ∈ {0,1,2}, G ∈ {0,1,2,3,4}:

Forward Map

A' = A
B' = (B + A) mod 3
G' = (G + B) mod 5


Inverse Map

A = A'
B = (B' - A') mod 3
G = (G' - B)  mod 5


Properties

Triangular form ⇒ automatically bijective

Domain = 45 states

No energy cost (ΔS_env = 0)

Hamiltonian-compatible

Pentary Reversible Mapping (ℤ₅³)

For A, B, G ∈ {0..4}:

Forward

A' = A
B' = (B + A) mod 5
G' = (G + B) mod 5


Inverse

A = A'
B = (B' - A') mod 5
G = (G' - B)  mod 5


Domain = 125 states, perfectly reversible.

⚛ Pentavalent Cycle

The Λ-gate participates in the five-phase RHEA cycle:

Ψ — Perception        : A_in
Φ — Internal Model    : B_in
Δ — Adaptive Delta    : B_out - B_in
T — Trust Update      : G_out - B_in
S — Entropy State     : G_in


ASCII diagram:

          Ψ (A_in)
             ↓
          Φ (B_in)
             ↓
          Δ (ΔB)
             ↓
          T (ΔG)
             ↓
          S (Entropy/Glyph)
             ↑
      — RHEA-Λ Hamiltonian Loop —

♇ Verilog Implementation (Behavioral)
module rhea_reversible_gate #(
    parameter DATA_WIDTH_BIN = 1
)(
    input  wire [1:0] mode,   // 00 binary, 01 ternary, 10 pentary
    input  wire [2:0] A_in,
    input  wire [2:0] B_in,
    input  wire [2:0] G_in,
    output reg  [2:0] A_out,
    output reg  [2:0] B_out,
    output reg  [2:0] G_out
);

// mod-3
function [1:0] add_mod3;
    input [1:0] x, y;
    reg [2:0] s;
    begin
        s = x + y;
        add_mod3 = (s >= 3) ? s - 3 : s[1:0];
    end
endfunction

// mod-5
function [2:0] add_mod5;
    input [2:0] x, y;
    reg [3:0] s;
    begin
        s = x + y;
        add_mod5 = (s >= 5) ? s - 5 : s[2:0];
    end
endfunction

always @* begin
    case (mode)
        2'b00: begin // binary
            A_out = {2'b00, ~(A_in[0] & B_in[0])};
            B_out = 3'b000;
            G_out = G_in;
        end
        2'b01: begin // ternary
            A_out = {1'b0, A_in[1:0]};
            B_out = {1'b0, add_mod3(B_in[1:0], A_in[1:0])};
            G_out = add_mod5(G_in, {1'b0, B_in[1:0]});
        end
        2'b10: begin // pentary
            A_out = A_in;
            B_out = add_mod5(B_in, A_in);
            G_out = add_mod5(G_in, B_in);
        end
        default: begin
            A_out = A_in;
            B_out = B_in;
            G_out = G_in;
        end
    endcase
end

endmodule

🧪 Reversibility Validation (Python)
def ternary_step(A,B,G):
    return A, (B+A)%3, (G+B)%5

def pentary_step(A,B,G):
    return A, (B+A)%5, (G+B)%5

def check_bijective(step_fn, sizes):
    nA,nB,nG = sizes
    seen={}
    for A in range(nA):
        for B in range(nB):
            for G in range(nG):
                out=step_fn(A,B,G)
                if out in seen:
                    print("Collision:", (A,B,G), "vs", seen[out])
                    return
                seen[out]=(A,B,G)
    print("Mapping is bijective over",nA*nB*nG,"states.")

👑 Synthesis

Works with:

Yosys

Vivado

Quartus

Cadence Genus

Example:

yosys -p "read_verilog src/rhea_reversible_gate.v; synth -top rhea_reversible_gate; write_verilog synth.v"

⚕ License — RHEA-Core Public Grant v1.0

Attribution Required

No Derivatives

No Military or Commercial Use Without Explicit License

Copyright © 2025

Sovereign IP — EnigmaticGlitch

Full license in LICENSE.

🜂 Author

Paul M. Roe (SovereignGlitch)
Architect of RHEA-UCM, Zadeian Sentinel, RHEA-Crypt
TecKnows, Inc. — Lewiston, Maine, USA

ORCID: 0009-0005-6159-947X
U.S. Provisional Patent: #63/796,404
⚕🜂 “We don’t fight entropy. We shape it.”

📚 Citation
Roe, P. M. (2025).
A Reversible Multi-Radix Computational Cell for Hamiltonian Symbolic Processing 
in the RHEA-UCM Framework.
Zenodo. https://doi.org/10.5281/zenodo.17783138

♛ Welcome to the Pentavalent Era.
⚕🜂♇ Post-Landauer computing begins here.
