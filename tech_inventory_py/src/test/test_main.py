import unittest
import main

from inventory import Inventory

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory("test_data.json")

    def test_inv_instance(self):
        self.assertEqual(self.inv, {}, "non-empty inventory before load is called")


if __name__ == "__main__":
    unittest.main()