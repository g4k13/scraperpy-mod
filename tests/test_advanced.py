# -*- coding: utf-8 -*-

from .context import scraperpy

import unittest, json


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_json_getBBCArabic(self):
        """getBBCArabic returns valid json document as a string"""
        self.assertTrue(scraperpy.is_json(scraperpy.getBBCArabic()))


if __name__ == '__main__':
    unittest.main()
