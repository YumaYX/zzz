import unittest
import zzz


class TestZzz(unittest.TestCase):

    def test_zzz(self):
        self.assertEqual(r"Zzz...", zzz.zzz())

    def test_block_text(self):
        file_name = r"tests/block_text.txt"
        header_pattern = r"^header"
        obj = zzz.block_text(file_name, header_pattern)

        expected_headers = [f"header{i}" for i in range(3)]
        expected_values = [["a"], ["b", "c"], ["d", "e", "f"]]

        for i in range(len(obj)):
            with self.subTest(index=i):
                self.assertEqual(expected_headers[i], obj[i].key)
                self.assertEqual(expected_values[i], obj[i].values)


if __name__ == "__main__":
    unittest.main()
