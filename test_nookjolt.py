# test_nookjolt.py
"""
Tests for NookJolt module.
"""

import unittest
from nookjolt import NookJolt

class TestNookJolt(unittest.TestCase):
    """Test cases for NookJolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NookJolt()
        self.assertIsInstance(instance, NookJolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NookJolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
