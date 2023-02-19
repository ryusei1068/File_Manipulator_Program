import unittest

import file_manipulator

class TestFileManipulator(unittest.TestCase):

    def test_verify_file_extend(self):
        path = 'files/test.txt'
        self.assertEqual(True, file_manipulator.verify_file_extend(path, len(path) - 4 ,'.txt'))
        self.assertEqual(False, file_manipulator.verify_file_extend(path, len(path) - 4 ,'.jpg'))


    def test_verify_arguments(self):
        with self.assertRaises(SystemExit):
            file_manipulator.verify_arguments(2, ['files/test.txt'])


if __name__ == '__main__':
    unittest.main()