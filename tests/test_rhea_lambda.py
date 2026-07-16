from __future__ import annotations

import unittest

from reference.rhea_lambda import (
    assert_bijection,
    pentary_forward,
    pentary_inverse,
    ternary_forward,
    ternary_inverse,
)


class LambdaMapTests(unittest.TestCase):
    def test_ternary_mixed_radix_bijection(self) -> None:
        assert_bijection(ternary_forward, ternary_inverse, (3, 3, 5))

    def test_pentary_bijection(self) -> None:
        assert_bijection(pentary_forward, pentary_inverse, (5, 5, 5))

    def test_inverse_uses_recovered_original_b(self) -> None:
        state = (2, 1, 4)
        encoded = ternary_forward(state)
        self.assertEqual(ternary_inverse(encoded), state)

    def test_invalid_unused_hdl_codes_rejected(self) -> None:
        with self.assertRaises(ValueError):
            ternary_forward((3, 0, 0))
        with self.assertRaises(ValueError):
            pentary_forward((0, 5, 0))


if __name__ == "__main__":
    unittest.main()
