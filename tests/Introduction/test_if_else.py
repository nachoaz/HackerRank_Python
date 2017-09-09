# test_if_else.py

import pathmagic
import if_else
from unittest.mock import patch

def test_if_else(capfd):
    io_pairs = [(['3'], 'Weird\n'), 
                (['24'], 'Not Weird\n'),
                (['2'], 'Not Weird\n'),
                (['20'], 'Weird\n'),
                (['21'], 'Weird\n'),
                (['22'], 'Not Weird\n'),
                (['8'], 'Weird\n'),
                (['98'], 'Not Weird\n'),
                (['99'], 'Weird\n')
                ]

    for user_input, expected_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            if_else.main()
            out, _ = capfd.readouterr()
            assert out == expected_output

