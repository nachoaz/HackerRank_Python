# test_tuples.py

import pathmagic
import tuples
from unittest.mock import patch


def test_tuples(capfd):
    io_pairs = [(['2', '1 2'], '3713081631934410656\n'),
                (['2', '1 4'], '3713081631940905806\n'),
                (['4', '3 9 2 8'], '-5908017774055513711\n')
                ]

    for user_input, correct_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            tuples.main()
            out, _ = capfd.readouterr()
            assert out == correct_output
