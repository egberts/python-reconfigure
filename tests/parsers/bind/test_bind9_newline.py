#!/usr/bin/env python3
from reconfigure.parsers import BIND9Parser
from reconfigure.nodes import *
import pytest
import unittest
import operator

class BIND9ParserCommentTest (unittest.TestCase):

  @classmethod
  def setUp(self):
    self.parser = BIND9Parser()
    print(self.parser.tokens[7])
    print(dir(self.parser.tokens[7]))
    token_tuple = self.parser.tokens[7]
    token_list = list(token_tuple)
    token_list[0] = r'\/\/([^\n]*\n*)'
    token_tuple = tuple(token_list)
    #self.parser.tokens[7] = token_tuple

  def test_inline_double_slashes(self):
    source = """
"""
    expected_parsed = RootNode( None,
                       Node( 'newline'
                           )
                     )
    actual_parsed = self.parser.parse(source)
    print("expected_parsed: ", expected_parsed)
    print("actual_parsed: ", actual_parsed)
    print("type expected_parsed: ", type(expected_parsed))
    print("type actual_parsed: ", type(actual_parsed))
    self.assertTrue(actual_parsed, expected_parsed)

  def __shutdown__(self, options):
    del BaseParserTest

# Standalone test support
if __name__ == '__main__':
    unittest.main()
