# finding_the_percentage.py

import pathmagic
import finding_the_percentage
from unittest.mock import patch


def test_finding_the_percentage(capfd):
    io_pairs = [(['3',
                  'Krishna 67 68 69',
                  'Arjun 70 98 63',
                  'Malika 52 56 60',
                  'Malika'], '56.00\n')]

    for user_input, correct_output in io_pairs:
        with patch('builtins.input', side_effect=user_input):
            finding_the_percentage.main()
            out, _ = capfd.readouterr()
            assert out == correct_output
