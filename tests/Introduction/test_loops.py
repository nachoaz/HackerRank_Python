# test_loops.py

import pathmagic
import loops
from unittest.mock import patch


def test_loops(capfd):
    io_pairs = [(['5'], '0\n1\n4\n9\n16\n'),
                (['4'], '0\n1\n4\n9\n'),
                (['9'], '0\n1\n4\n9\n16\n25\n36\n49\n64\n')
               ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            loops.main()
            out, _ = capfd.readouterr()
            assert out == expected_output
