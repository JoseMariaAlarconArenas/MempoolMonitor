# test_mempoolmonitor.py
"""
Tests for MempoolMonitor module.
"""

import unittest
from mempoolmonitor import MempoolMonitor

class TestMempoolMonitor(unittest.TestCase):
    """Test cases for MempoolMonitor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MempoolMonitor()
        self.assertIsInstance(instance, MempoolMonitor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MempoolMonitor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
