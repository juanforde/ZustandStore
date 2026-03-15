# test_zustandstore.py
"""
Tests for ZustandStore module.
"""

import unittest
from zustandstore import ZustandStore

class TestZustandStore(unittest.TestCase):
    """Test cases for ZustandStore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZustandStore()
        self.assertIsInstance(instance, ZustandStore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZustandStore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
