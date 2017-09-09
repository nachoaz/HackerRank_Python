# test_write_a_function.py

import pathmagic
import write_a_function
from unittest.mock import patch


def test_python_division(capfd):
    io_pairs = [(['1990'], 'False\n'),
                (['2000'], 'True\n'),
                (['2400'], 'True\n'),
                (['1800'], 'False\n'),
                (['2004'], 'True\n')
                ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            write_a_function.main()
            out, _ = capfd.readouterr()
            assert out == expected_output
