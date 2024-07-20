import unittest
import zzz2


class TestZzz2(unittest.TestCase):

    def test_sheet_to_text(self):
        expect = "key\nvalue\n1.0\na\n2.0\nb\n3.0\nc\n4.0\nd\n5.0\ne\n6.0\nf"

        book = r"tests/book.xlsx"
        sheet = r"mysheet"

        self.assertEqual(expect, zzz2.sheet_to_text(book, sheet, 8, 2))


if __name__ == "__main__":
    unittest.main()
