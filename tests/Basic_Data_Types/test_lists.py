# test_lists.py

import pathmagic
import lists
from unittest.mock import patch


def test_lists(capfd):
    io_pairs = [(['12',
                  'insert 0 5',
                  'insert 1 10',
                  'insert 0 6',
                  'print',
                  'remove 6',
                  'append 9',
                  'append 1',
                  'sort',
                  'print',
                  'pop',
                  'reverse',
                  'print'], '[6, 5, 10]\n[1, 5, 9, 10]\n[9, 5, 1]\n')]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            lists.main()
            out, _ = capfd.readouterr()
            assert out == expected_output
