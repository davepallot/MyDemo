import unittest
from MyDemo.Math import Math

class TestMymath(unittest.TestCase):

    def test_square(self):
        m = Math()
        self.assertEqual(m.square(10), 100)
        self.assertNotEqual(m.square(7), 48)

if __name__ == '__main__':
    unittest.main()

