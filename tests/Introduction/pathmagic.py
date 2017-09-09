"""
Path hack to make tests work.

From: http://bit.ly/2xSlEMG
"""

import os
import sys

subdomain = os.path.realpath('.').split(os.sep)[-1]
modpath = os.sep.join(os.path.realpath('.').split(os.sep)[:-2]) \
          + '/src/' \
          + subdomain

sys.path.insert(0, modpath)
