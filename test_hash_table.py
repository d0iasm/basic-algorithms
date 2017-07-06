import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        hash_table = HashTable(3)
        hash_table.add("key1", "val1")
        hash_table.add("key2", "val2")
        hash_table.add("key3", "val3")
        hash_table.add("", "val_blank")
        hash_table.add("key_none", None)
        hash_table.delete("key2")
        self.assertEqual("val1", hash_table.get("key1"))
        self.assertEqual("val_blank", hash_table.get(""))
        self.assertIsNone(hash_table.get("key_none"))
        self.assertIsNone(hash_table.get("key2"))
        self.assertIsNone(hash_table.get("hoge"))
        self.assertRaises(Exception, hash_table.get, None)

    def test_invalid_size(self):
        self.assertRaises(Exception, HashTable, 0)

        
if __name__ == '__main__':
    unittest.main()
