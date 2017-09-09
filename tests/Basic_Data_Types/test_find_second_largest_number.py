# test_find_second_largest_number.py

import pathmagic
import find_second_largest_number
from unittest.mock import patch


def test_find_second_largest_number(capfd):
    io_pairs = [(['5', '2 3 6 6 5'], '5\n'),
                (['8', '2 3 6 6 6 6 9 8'], '8\n'),
                (['3', '1 2 2'], '1\n'),
                (['4', '1 1 1 1'], '1\n'),
                (['2', '8 99'], '8\n')
               ]

    for user_input, correct_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            find_second_largest_number.main()
            out, _ = capfd.readouterr()
            assert out == correct_output
