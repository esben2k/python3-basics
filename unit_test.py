#unit_test.py

import unittest

from test_function_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for the test_funtion_1.py"""

	def test_first_last_name(self):
		formatted_name = get_formatted_name('joe','schmo')
		self.assertEqual(formatted_name, 'Joe Schmo')# the expected result to test towards

unittest.main()