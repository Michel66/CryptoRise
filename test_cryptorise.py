# test_cryptorise.py
"""
Tests for CryptoRise module.
"""

import unittest
from cryptorise import CryptoRise

class TestCryptoRise(unittest.TestCase):
    """Test cases for CryptoRise class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoRise()
        self.assertIsInstance(instance, CryptoRise)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoRise()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
