# test_hello_world.py

import pathmagic
import hello_world


def test_hello_world(capfd):
    hello_world.main()
    out, _ = capfd.readouterr()
    assert out == 'Hello, World!\n'
