# test_python_division.py

import pathmagic
import python_division
from unittest.mock import patch


def test_python_division(capfd):
    io_pairs = [(['4', '3'], '1\n1.3333333333333333\n'),
                (['3', '2'], '1\n1.5\n'),
                (['45', '9'], '5\n5.0\n')
                ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            python_division.main()
            out, _ = capfd.readouterr()
            assert out == expected_output
