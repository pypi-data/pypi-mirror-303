#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Tests for `modifiedstemmer` module.
"""
import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src/mod_stemmer')))
from modifiedstemmer import stemmer


class Test_Modified_stemmer(unittest.TestCase):

    def setUp(self):
        pass

    def test_stem(self):
        st = stemmer()

        with open('tests.csv') as test_cases:
            for line in test_cases:
                orig, stemmed = line.strip().split(',')
                self.assertEqual(st.stem(orig), stemmed)

        test_cases.close()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()