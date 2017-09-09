# test_arithmetic_operators.py

import pathmagic
import arithmetic_operators
from unittest.mock import patch


def test_arithmetic_operators(capfd):
    io_pairs = [(['3', '2'], '5\n1\n6\n'),
                (['4', '1'], '5\n3\n4\n'),
                (['8', '12'], '20\n-4\n96\n')
                ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
                arithmetic_operators.main()
                out, _ = capfd.readouterr()
                assert out == expected_output
