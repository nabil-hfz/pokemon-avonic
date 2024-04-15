import unittest

from utils.formatter import Formatter


class TestFormatter(unittest.TestCase):

    def test_format_name(self):
        """Test the formatting of names."""
        self.assertEqual(Formatter.format_name(" alice "), "Alice")
        self.assertEqual(Formatter.format_name("bOB"), "Bob")
        self.assertEqual(Formatter.format_name(" CHARLES "), "Charles")

    def test_format_damage(self):
        """Test the formatting of damage values."""
        self.assertEqual(Formatter.format_damage(25.555), "25.6")
        self.assertEqual(Formatter.format_damage(100.0), "100.0")
        self.assertEqual(Formatter.format_damage(3.14159), "3.1")

    def test_format_health(self):
        """Test the formatting of health values."""
        self.assertEqual(Formatter.format_health(199.99), "200.0")
        self.assertEqual(Formatter.format_health(0.1), "0.1")
        self.assertEqual(Formatter.format_health(87.5), "87.5")

    def test_format_percentage(self):
        """Test the formatting of percentage values."""
        self.assertEqual(Formatter.format_percentage(99.999), "100.00%")
        self.assertEqual(Formatter.format_percentage(0.1234), "0.12%")
        self.assertEqual(Formatter.format_percentage(25.3456), "25.35%")
