import unittest

from slupy.file_ops import file_ops


class TestFileOps(unittest.TestCase):

    def test_get_extension_from_filepath(self):
        self.assertEqual(file_ops.get_extension_from_filepath("hello1.csv"), "csv")
        self.assertEqual(file_ops.get_extension_from_filepath("hello2.XLSX"), "XLSX")
        self.assertEqual(file_ops.get_extension_from_filepath("hello3.txt"), "txt")

    def test_get_basename_from_filepath(self):
        self.assertEqual(
            file_ops.get_basename_from_filepath("users/username/folder/some-file.txt"),
            "some-file.txt",
        )

    def test_filter_filepaths_by_extensions(self):
        result = file_ops.filter_filepaths_by_extensions(
            filepaths=['one.js', 'two.py', 'three.css', 'four.go', 'five.html', 'six.py', 'seven.js'],
            extensions=['css', 'js'],
        )
        self.assertEqual(
            result,
            ['one.js', 'three.css', 'seven.js'],
        )

