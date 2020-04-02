class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TrieNode:
    def __init__(self, x):
        self.val = x
        self.childrens = [None] * 26
