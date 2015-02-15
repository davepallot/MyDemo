import unittest
import Math

class TestMymath(unittest.TestCase):

    def test_square(self):
        m = Math.Math()
        self.assertEqual(m.square(10), 100)

if __name__ == '__main__':
    unittest.main()

