#!/usr/bin/env python3
from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Paulina, Ansaa"
        expected = "Ansaa Paulina"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        """edge cases are input to our code that produces unexpected 
        results
        """
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_names(self):
        testcase = "Paulina, Ansaa A."
        expected = "Ansaa A. Paulina"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Hamilton"
        expected = "Hamilton"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
