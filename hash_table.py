#!/usr/bin/env python3

# HashTable
# 衝突回避 チェイン法
# 時間計算量 挿入 O(1) 検索 O(1) 削除 O(1)
# 空間計算量 O(n+m) n=テーブルの大きさ m=エントリリストの数

class HashTable(object):
    class Cell(object):
        def __init__(self, key, value, next=None):
            self.key = key
            self.value = value
            self.next = next

            
    def __init__(self, size):
        if size == 0: raise Exception("size is invalid value")
        self.size = size
        self.table = [None] * self.size

        
    def _hash(self, key):
        return hash(key) % self.size

    def _get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True, current
            current = current.next

        return False, index

    
    def get(self, key):
        if key is None: raise Exception("Key is None")

        is_exist, cell = self._get(key)
        if is_exist: return cell.value
        return None

    
    def add(self, key, value):
        if key is None: raise Exception("Key is None")
        
        is_exist, cell = self._get(key)
        if is_exist:
            cell.value = value
        else:
            new = HashTable.Cell(key, value, self.table[self._hash(key)])
            self.table[self._hash(key)] = new
    
    
    def delete(self, key):
        if key is None: raise Exception("Key is None")

        index = self._hash(key)
        current = self.table[index]

        if current.key == key:
            self.table[index] = current.next
            return
        
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next
                
        
