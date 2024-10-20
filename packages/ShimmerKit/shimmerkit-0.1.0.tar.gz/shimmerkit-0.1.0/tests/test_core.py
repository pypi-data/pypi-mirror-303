# tests/test_core.py

import unittest
from core import CoreFunctionality

class TestCoreFunctionality(unittest.TestCase):
    def test_process(self):
        core = CoreFunctionality("test data")
        self.assertEqual(core.process(), "Processed: test data")

if __name__ == '__main__':
    unittest.main()
