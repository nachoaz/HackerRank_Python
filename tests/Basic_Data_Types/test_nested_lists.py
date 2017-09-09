# test_nested_lists.py

import pathmagic
import nested_lists
from unittest.mock import patch


def test_nested_lists(capfd):
    io_pairs = [(['5', 
                  'Harry',
                  '37.21',
                  'Berry',
                  '37.21',
                  'Tina',
                  '37.2',
                  'Akriti',
                  '41',
                  'Harsh',
                  '39'], 'Berry\nHarry\n')]

    for user_input, correct_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            nested_lists.main()
            out, _ = capfd.readouterr()
            assert out == correct_output
