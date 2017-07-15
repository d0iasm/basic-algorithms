import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def test_queue_size(self):
        queue = Queue(3)
        self.assertTrue(queue.is_empty())
        self.assertFalse(queue.is_full())
        queue.enqueue("val1")
        queue.enqueue("val2")
        queue.enqueue("val3")
        self.assertFalse(queue.is_empty())
        self.assertTrue(queue.is_full())

    def test_dequeue(self):
        queue = Queue(3)
        queue.enqueue("val1")
        queue.enqueue("val2")
        self.assertEqual("val1", queue.dequeue())
        self.assertEqual("val2", queue.dequeue())
        
        
    def test_underflow(self):
        queue = Queue(3)
        self.assertRaises(Exception, queue.dequeue)

        
    def test_overflow(self):
        queue = Queue(3)
        queue.enqueue("val1")
        queue.enqueue("val2")
        queue.enqueue("val3")
        self.assertRaises(Exception, queue.enqueue, "val4")
        
    def test_invalid_enqueue(self):
        queue = Queue(3)
        self.assertRaises(Exception, queue.enqueue, None)

        
    def test_invalid_size(self):
        self.assertRaises(Exception, Queue, 0)

        
if __name__ == '__main__':
    unittest.main()
