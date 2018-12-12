#!/usr/bin/env python3
from reconfigure.nodes import *
import pytest
import unittest
import operator


class BaseOperatorTest (unittest.TestCase):

  @classmethod
  def setUp(self):
    pass

  def test_operator_eq(self):
    expected_parsed = RootNode( None,
                       Node( 'comment',
                             PropertyNode('', '// hashtag comment line\n')
                           )
                     )
    actual_parsed = RootNode( None )
    self.assertFalse(actual_parsed == expected_parsed)

  def test_operator_ne(self):
    expected_parsed = RootNode( None,
                       Node( 'comment',
                             PropertyNode('', '// hashtag comment line\n')
                           )
                     )
    actual_parsed = RootNode( None )
    self.assertTrue(actual_parsed != expected_parsed)

  def __shutdown__(self, options):
    del BaseOperatorTest

# Standalone test support
if __name__ == '__main__':
    unittest.main()
