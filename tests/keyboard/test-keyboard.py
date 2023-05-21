#!/usr/bin/env python3
# Copyright © 2018 Red Hat, Inc
#             2021 Sebastian Keller
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# Authors: Benjamin Berg <bberg@redhat.com>
#          Sebastian Keller <skeller@gnome.org>

import os
import sys
import unittest

try:
    import dbusmock
except ImportError:
    sys.stderr.write('You need python-dbusmock (http://pypi.python.org/pypi/python-dbusmock) for this test suite.\n')
    sys.exit(1)

# Add the shared directory to the search path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

from gtest import GTest
from x11session import X11SessionTestCase

BUILDDIR = os.environ.get('BUILDDIR', os.path.join(os.path.dirname(__file__)))


class PanelTestCase(X11SessionTestCase, GTest):
    g_test_exe = os.path.join(BUILDDIR, 'test-keyboard-shortcuts')


if __name__ == '__main__':
    # avoid writing to stderr
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout, verbosity=2))
