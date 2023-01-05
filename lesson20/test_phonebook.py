import unittest
import phonebook

class TestPhonebook(unittest.TestCase):

    def test(self):
        self.assertIsInstance(phonebook.open_file(), dict)


if __name__ == '__main__':
    unittest.main()