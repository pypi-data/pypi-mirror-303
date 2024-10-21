import unittest
import os
import shutil
import configparser
from yet_another_simple_file_sorter_ashaider.config import create_default_config, read_config_file

class TestConfig(unittest.TestCase):

    def setUp(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.config_file_path = os.path.join(current_directory, 'test_config.ini')

    def tearDown(self):
        if os.path.exists(self.config_file_path):
            os.remove(self.config_file_path)

    def test_create_default_config(self):
        created = create_default_config(self.config_file_path)
        self.assertTrue(created)

        self.assertTrue(os.path.exists(self.config_file_path))

        config = configparser.ConfigParser()
        config.read(self.config_file_path)

    def test_read_config_file(self):
        create_default_config(self.config_file_path)

        try:
            read_config_file(self.config_file_path, None)
            self.assertTrue(True)
        except Exception:
            self.fail("read_config_file raised Exception unexpectedly!")

if __name__ == '__main__':
    unittest.main()
