import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'pyhton'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Pyhton')

    def test_two_word(self):
        text = 'python snake'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python Snake')


if __name__ == '__main__':
    unittest.main