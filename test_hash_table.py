import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_hash(self):
        hash_table = HashTable(10)
        hash_table.add("key1", "val1")
        hash_table.add("key2", "val2")
        # hash_table.add("key3", "val3")
        hash_table.delete("key2")
        self.assertEqual("val1", hash_table.get("key1"))
        self.assertIsNone(hash_table.get("key2"))
        self.assertIsNone(hash_table.get("hoge"))


if __name__ == '__main__':
    unittest.main()
