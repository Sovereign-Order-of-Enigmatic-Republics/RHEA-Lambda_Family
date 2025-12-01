// ======================================================
// RHEA-UCM Reversible Multi-Radix Gate
// Author: Paul M. Roe (TecKnows, Inc.)
// Date:   December 1, 2025
// Prior art established: https://github.com/Sovereign-Order-of-Enigmatic-Republics/RHEA-Reversible-Cell
// License: RHEA-Core Public Grant v1.0 (see LICENSE)
// ======================================================

module rhea_reversible_gate #(
    parameter DATA_WIDTH_BIN = 1
)(
    input  wire [1:0] mode,   // 00 = binary, 01 = ternary, 10 = pentary
    input  wire [2:0] A_in,   // Symbolic operand Ψ (up to pentary: 0..4)
    input  wire [2:0] B_in,   // Symbolic operand Φ (up to pentary: 0..4)
    input  wire [2:0] G_in,   // Glyph / entropy / trust register (0..4)
    output reg  [2:0] A_out,
    output reg  [2:0] B_out,
    output reg  [2:0] G_out
);

    // --------------------------------------------------
    // Modular arithmetic helpers
    // --------------------------------------------------
    function automatic [1:0] add_mod3;
        input [1:0] x, y;
        reg   [2:0] sum;
        begin
            sum = x + y;
            add_mod3 = (sum >= 3) ? sum - 3 : sum[1:0];
        end
    endfunction

    function automatic [2:0] add_mod5;
        input [2:0] x, y;
        reg   [3:0] sum;
        begin
            sum = x + y;
            add_mod5 = (sum >= 5) ? sum - 5 : sum[2:0];
        end
    endfunction

    // --------------------------------------------------
    // Main combinatorial logic
    // --------------------------------------------------
    always @* begin
        case (mode)
            2'b00: begin // Binary irreversible mode (CMOS-compatible NAND example)
                A_out = {2'b00, ~(A_in[0] & B_in[0])}; // Result on A_out[0]
                B_out = 3'b000;
                G_out = G_in;                         // Glyph preserved
            end

            2'b01: begin // Ternary reversible mode (ℤ₃ × ℤ₃ × ℤ₅)
                A_out = {1'b0, A_in[1:0]};                          // A' = A
                B_out = {1'b0, add_mod3(B_in[1:0], A_in[1:0])};     // B' = B + A (mod 3)
                G_out = add_mod5(G_in, {1'b0, B_in[1:0]});          // G' = G + B (mod 5)  (original B)
            end

            2'b10: begin // Pentary reversible mode (ℤ₅³)
                A_out = A_in;                                      // A' = A
                B_out = add_mod5(B_in, A_in);                      // B' = B + A (mod 5)
                G_out = add_mod5(G_in, B_in);                      // G' = G + B (mod 5)  (original B)
            end

            default: begin // Safe pass-through
                A_out = A_in;
                B_out = B_in;
                G_out = G_in;
            end
        endcase
    end

endmodule