import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_stack_size(self):
        stack = Stack(3)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push("val1")
        stack.push("val2")
        stack.push("val3")
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())

    def test_pop(self):
        stack = Stack(3)
        stack.push("val1")
        stack.push("val2")
        self.assertEqual("val2", stack.pop())
        self.assertEqual("val1", stack.pop())
        
        
    def test_underflow(self):
        stack = Stack(3)
        self.assertRaises(Exception, stack.pop)

        
    def test_overflow(self):
        stack = Stack(3)
        stack.push("val1")
        stack.push("val2")
        stack.push("val3")
        self.assertRaises(Exception, stack.push, "val4")
        
    def test_invalid_push(self):
        stack = Stack(3)
        self.assertRaises(Exception, stack.push, None)

        
    def test_invalid_size(self):
        self.assertRaises(Exception, Stack, 0)

        
if __name__ == '__main__':
    unittest.main()
