import unittest
import os
import shutil
from yasfs.file_organizer import organize_files

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.source = 'test_source'
        self.destination = 'test_destination'
        os.makedirs(self.source, exist_ok=True)
        os.makedirs(self.destination, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.source)
        shutil.rmtree(self.destination)

    def test_organize_files(self):
        test_file_path = os.path.join(self.source, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('A kilogram of bricks vs a kilogram of feathers, who would win?')

        organize_files(self.source, self.destination, False, set(), {})

        self.assertFalse(os.path.exists(test_file_path))
        self.assertTrue(os.path.exists(os.path.join(self.destination, 'TXT_Files', 'test_file.txt')))

    def test_organize_files_no_destination(self):
        test_file_path = os.path.join(self.source, 'test_file2.txt')
        with open(test_file_path, 'w') as f:
            f.write('The answer is Satoru Gojo. He would win.')

        organize_files(self.source, self.destination, True, set(), {})

        self.assertTrue(os.path.exists(test_file_path))

if __name__ == '__main__':
    unittest.main()
