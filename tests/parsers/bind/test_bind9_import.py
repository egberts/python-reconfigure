#!/usr/bin/env python3
import unittest
import sys
import logging

#
# Caveats:
# - Do not call sys.exit(), let it run its course out the unittest.main()
#

class BIND9ParserImportTest (unittest.TestCase):

  def test_bind9_parser_import(self):
    """ Exercise import of BIND9Parser module """
    try:
        from reconfigure.parsers import BIND9Parser
    except ImportError:
        print("FAIL: Python BIND9Parser module is not importable")
        self.assertTrue(False)
    except ImportWarning:
        print("FAIL: Python BIND9Parser module has warnings")
        self.assertTrue(False)
    except:
        print("FAIL: Python BIND9Parser module triggered non-import exception")
        self.assertTrue(False)


# Standalone test support
if __name__ == '__main__':
  VERBOSE = '-v' in sys.argv
  logging.basicConfig(level=logging.DEBUG if VERBOSE else logging.ERROR)
  unittest.main()
