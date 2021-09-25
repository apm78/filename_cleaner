import unittest

import filename_cleaner as cleaner


class TestFindFileWithNonAsciiName(unittest.TestCase):
    def test_check_filename(self):
        self.assertEqual(True, cleaner.check_filename('Würste'))
        self.assertEqual(True, cleaner.check_filename('Überall'))
        self.assertEqual(True, cleaner.check_filename('Käse'))
        self.assertEqual(True, cleaner.check_filename('Ändern'))
        self.assertEqual(True, cleaner.check_filename('Gönner'))
        self.assertEqual(True, cleaner.check_filename('Österreich'))
        self.assertEqual(True, cleaner.check_filename('Muße'))
        self.assertEqual(False, cleaner.check_filename('Wurst'))
        self.assertEqual(False,
                         cleaner.check_filename('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+_&'))

    def test_new_filename(self):
        self.assertEqual(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+_&',
            cleaner.new_filename('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+_&'))
        self.assertEqual(
            'AeOeUeaeoeuess_',
            cleaner.new_filename('ÄÖÜäöüßé'))
        self.assertEqual('toestFile.txt', cleaner.new_filename('töstFile.txt'))


if __name__ == '__main__':
    unittest.main()
