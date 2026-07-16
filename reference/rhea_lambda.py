"""Canonical finite-domain RHEA-Lambda reference maps.

The mixed-radix map is triangular: recover A first, then original B, then G.
All functions reject invalid encoded states instead of silently operating on the
unused bit patterns present on the wider HDL ports.
"""

from __future__ import annotations

from itertools import product
from typing import Iterable, Iterator, Tuple

State = tuple[int, int, int]


def _require_state(state: State, radices: State) -> State:
    if len(state) != 3:
        raise ValueError("state must contain exactly three coordinates")
    for value, radix in zip(state, radices):
        if not isinstance(value, int) or not 0 <= value < radix:
            raise ValueError(f"invalid state {state!r} for radices {radices!r}")
    return state


def ternary_forward(state: State) -> State:
    a, b, g = _require_state(state, (3, 3, 5))
    return a, (b + a) % 3, (g + b) % 5


def ternary_inverse(state: State) -> State:
    a_out, b_out, g_out = _require_state(state, (3, 3, 5))
    a = a_out
    b = (b_out - a) % 3
    g = (g_out - b) % 5
    return a, b, g


def pentary_forward(state: State) -> State:
    a, b, g = _require_state(state, (5, 5, 5))
    return a, (b + a) % 5, (g + b) % 5


def pentary_inverse(state: State) -> State:
    a_out, b_out, g_out = _require_state(state, (5, 5, 5))
    a = a_out
    b = (b_out - a) % 5
    g = (g_out - b) % 5
    return a, b, g


def states(radices: State) -> Iterator[State]:
    yield from product(*(range(radix) for radix in radices))


def assert_bijection(forward, inverse, radices: State) -> None:
    domain = tuple(states(radices))
    outputs = tuple(forward(state) for state in domain)
    if len(set(outputs)) != len(domain):
        raise AssertionError("forward map is not injective")
    for state in domain:
        if inverse(forward(state)) != state:
            raise AssertionError(f"inverse(forward({state})) failed")
    for state in outputs:
        if forward(inverse(state)) != state:
            raise AssertionError(f"forward(inverse({state})) failed")


if __name__ == "__main__":
    assert_bijection(ternary_forward, ternary_inverse, (3, 3, 5))
    assert_bijection(pentary_forward, pentary_inverse, (5, 5, 5))
    print("RHEA-Lambda canonical maps validated over 45 and 125 states.")
