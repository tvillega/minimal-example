import unittest

import main

class TestMyProgram(unittest.TestCase):

    def test_countdown(self):
        self.assertEqual(self.countdown(), -1)


if __name__ == '__main__':
    unittest.main()
