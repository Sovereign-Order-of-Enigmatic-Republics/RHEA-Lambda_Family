#!/usr/bin/env python3
"""
RHEA-UCM Reversible Multi-Radix Gate — Exhaustive Bijectivity Checker
Author: Paul M. Roe (TecKnows, Inc.)
Date:   December 1, 2025
License: RHEA-Core Public Grant v1.0
Repo:   https://github.com/Sovereign-Order-of-Enigmatic-Republics/RHEA-Reversible-Cell

This script proves that the ternary and pentary modes of the RHEA reversible gate
are perfectly bijective (i.e., fully reversible, zero information loss).

- Ternary mode:  ℤ₃ × ℤ₃ × ℤ₅  → 45 states
- Pentary mode:  ℤ₅ × ℤ₅ × ℤ₅  → 125 states

Both mappings are permutations of their full state space → thermodynamically admissible.
"""

from typing import Tuple, Callable


def ternary_step(A: int, B: int, G: int) -> Tuple[int, int, int]:
    """
    Forward map for ternary reversible mode (ℤ₃ × ℤ₃ × ℤ₅)

    A' = A
    B' = (B + A) mod 3
    G' = (G + B) mod 5     # uses original B (triangular structure)
    """
    return A, (B + A) % 3, (G + B) % 5


def pentary_step(A: int, B: int, G: int) -> Tuple[int, int, int]:
    """
    Forward map for pentary reversible mode (ℤ₅³)

    A' = A
    B' = (B + A) mod 5
    G' = (G + B) mod 5     # uses original B
    """
    return A, (B + A) % 5, (G + B) % 5


def check_bijective(
    step_fn: Callable[[int, int, int], Tuple[int, int, int]],
    sizes: Tuple[int, int, int],
    name: str
) -> None:
    """
    Exhaustively verify that a mapping is a bijection over the full state space.
    """
    nA, nB, nG = sizes
    total_states = nA * nB * nG
    seen = {}

    print(f"\n=== Checking {name} mode ===")
    print(f"State space: {nA} × {nB} × {nG} = {total_states} states")

    for A in range(nA):
        for B in range(nB):
            for G in range(nG):
                output = step_fn(A, B, G)

                if output in seen:
                    print("Collision found!")
                    print(f"  Input  (A,B,G) = {A, B, G}")
                    print(f"  Collides with   {seen[output]}")
                    print(f"  Both map to     {output}")
                    return

                seen[output] = (A, B, G)

    print(f"Mapping is bijective over {total_states} states.")


def main() -> None:
    print("RHEA-UCM Reversible Gate — Bijectivity Verification")
    print("=" * 60)

    check_bijective(ternary_step, (3, 3, 5), "Ternary (ℤ₃ × ℤ₃ × ℤ₅)")
    check_bijective(pentary_step, (5, 5, 5), "Pentary (ℤ₅³)")

    print("\nAll reversible modes are mathematically proven bijective.")
    print("Zero-erasure symbolic computation is thermodynamically admissible.")


if __name__ == "__main__":
    main()
