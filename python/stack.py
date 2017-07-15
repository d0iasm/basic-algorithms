#!/usr/bin/env python3

# Stack
# LIFO last-in, first-out
# 時間計算量 挿入O(1) 削除O(1)
# 空間計算量 O(size) size=スタックのサイズ, デフォルト1024


class Stack(object):
    def __init__(self, size=1024):
        if size == 0:
            raise Exception("Invalid size")
        self.size = size
        self.stack = [None] * self.size
        self.top = 0


    def is_empty(self):
        if self.stack[0] == None:
            assert self.top == 0, "Error: do not fit size"
            return True
        return False


    def is_full(self):
        if self.stack[self.size-1] is not None:
            assert self.top == self.size, "Error: do not fit size"
            return True
        return False


    def push(self, value):
        if self.is_full():
            raise Exception("オーバーフロー")
        if value is None:
            raise Exception("Invalid value")
        
        self.stack[self.top] = value
        self.top += 1


    def pop(self):
        if self.is_empty():
            raise Exception("アンダーフロー")

        value = self.stack[self.top-1]
        self.stack[self.top] = None
        self.top -= 1
        return value

    
