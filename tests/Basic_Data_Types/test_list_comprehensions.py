# test_list_comprehensions.py

import pathmagic
import list_comprehensions
from unittest.mock import patch


def test_list_comprensions(capfd):
    io_pairs = [(['1', '1', '1', '2'],
                  '[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]\n')
                ]

    for user_input, correct_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            list_comprehensions.main()
            out, _ = capfd.readouterr()
            assert out == correct_output
