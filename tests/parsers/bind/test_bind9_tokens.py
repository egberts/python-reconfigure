#!/usr/bin/env python3
import sys
import logging
from reconfigure.parsers import BIND9Parser
from reconfigure.nodes import *
import pytest
import unittest
import operator

class BIND9ParserCommentTest (unittest.TestCase):

  @classmethod
  def setUp(self):
    self.parser = BIND9Parser()
    print(self.parser.tokens)
    tokens = [
               (r'#([^\s\n]*.*)', lambda s, t: ('comment2', t)),
   #            (r'#([^\s\n]*.*)', lambda s, t: ('comment1', t)),
             ]
    print(self.parser.tokens[7])
    print(dir(self.parser.tokens[7]))
    print(tokens)
    self.parser.tokens = tokens
    # token_tuple = self.parser.tokens[7]
    # token_list = list(token_tuple)
    # token_list[0] = '\/\/([^\n]*\n*)'
    # token_tuple = tuple(token_list)
    #self.parser.tokens[7] = token_tuple

  def test_inline_double_slashes(self):
    source = """# hashtag comment line
"""
    expected_parsed = RootNode( None,
                       Node( 'comment',
                             PropertyNode('', '# hashtag comment line\n')
                           )
                     )
    import pdb; pdb.set_trace()
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
  VERBOSE = '-v' in sys.argv
  logging.basicConfig(level=logging.DEBUG if VERBOSE else logging.ERROR)
  unittest.main()
