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

    def test_to_ascii(self):
        self.assertEqual(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+_&',
            cleaner.to_ascii('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+_&'))
        self.assertEqual(
            'AeOeUeaeoeuessAEIOUaeiou',
            cleaner.to_ascii('ÄÖÜäöüßÁÉÍÓÚáéíóú'))
        self.assertEqual(
            'AeOeUeaeoeueAEIOUaeiou',
            cleaner.to_ascii('A\u0308O\u0308U\u0308a\u0308o\u0308u\u0308A\u0301E\u0301I\u0301O\u0301U\u0301a\u0301e\u0301i\u0301o\u0301u\u0301'))
        self.assertEqual('toestFile.txt', cleaner.to_ascii('töstFile.txt'))


if __name__ == '__main__':
    unittest.main()
