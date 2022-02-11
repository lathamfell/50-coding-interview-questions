#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'lf'
__date__ = '2022/02/11'

Implement a LIFO stack that has a push(), pop(), and max() function, where max() returns the maximum value in the stack. All of these functions should run in O(1) time.
'''


class MaxStack:
	def __init__(self):
		self.max = None
		self.head = Node()

	def push(self, val):
		n = Node(val)
		n.next = self.head.next
		self.head.next = n
		if self.max is None or val > self.max:
			# new max
			n.old_max = self.max
			self.max = val

	def pop(self):
		ret_node = self.head.next
		self.head.next = ret_node.next
		if ret_node.old_max is not None:
			self.max = ret_node.old_max
		return ret_node.val

	def max(self):
		return self.max


class Node:
	def __init__(self, val=None):
		self.val = val
		self.next = None
		self.old_max = None



if __name__ == '__main__':
    test = MaxStack()

    test.push(1)
    assert test.max() == 1
    test.push(2)
    assert test.max() == 2
    test.push(1)
    assert test.max() == 2
    assert test.pop() == 1
    assert test.max() == 2
    assert test.pop() == 2
    assert test.max() == 1
    assert test.pop() == 1

    try:
        test.max()
    except Exception as e:
        assert type(e) == ValueError

    try:
        test.pop()
    except Exception as e:
        assert type(e) == ValueError
