#!/usr/bin/env python3

# HashTable
# 衝突回避 チェイン法
# 時間計算量 挿入 O(1) 探索 O(1) 削除 O(1)
# 空間計算量

import sys

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size
    

    def add(self, key, value):
        self.table[self._hash(key)] = value

    def get(self, key):
        return self.table[self._hash(key)]

    def delete(self, key):
        self.table[self._hash(key)] = None
