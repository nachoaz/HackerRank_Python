# test_print_function.py

import pathmagic
import print_function
from unittest.mock import patch


def test_python_division(capfd):
    io_pairs = [(['3'], '123\n'),
                (['10'], '12345678910\n')
                ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            print_function.main()
            out, _ = capfd.readouterr()
            assert out == expected_output
