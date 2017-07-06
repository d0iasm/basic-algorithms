#!/usr/bin/env python3

# Queue
# FIFO first-in, first-out
# 時間計算量 挿入O(1) 削除O(1)
# 空間計算量 O(size) size=キューのサイズ, デフォルト1024


class Queue(object):
    def __init__(self, size=1024):
        if size == 0:
            raise Exception("Invalid size")
        self.size = size
        self.queue = [None] * self.size
        self.head = 0
        self.tail = 0


    def is_empty(self):
        if self.queue[self.head] is None:
            return True
        return False


    def is_full(self):
        if self.queue[self.tail] is not None:
            return True
        return False


    def enqueue(self, value):
        if self.is_full():
            raise Exception("オーバーフロー")
        if value is None:
            raise Exception("Invalid value")

        self.queue[self.tail] = value
        if self.tail == self.size - 1:
            self.tail = 0
        else:
            self.tail += 1


    def dequeue(self):
        if self.is_empty():
            raise Exception("アンダーフロー")

        value = self.queue[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return value

    
