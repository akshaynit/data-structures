# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 17:16:14 2019

@author: AK389016
"""

def insert(root, node):
    if root == None:
        return
    if root.data > node.data:
        if root.left == None:
            root.left = node
            return
        else:
            insert(root.left, node)
    if root.data <= node.data:
        if root.right == None:
            root.right = node
            return
        else:
            insert(root.right, node)
    
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
            
def inorderTraversal(root):
    if root == None:
        return
    print(root.data)
    inorderTraversal(root.left)
    inorderTraversal(root.right)

def preorderTraversal(root):
    if root == None:
        return
    preorderTraversal(root.left)
    print(root.data)
    preorderTraversal(root.right)

def postorderTraversal(root):
    if root == None:
        return
    postorderTraversal(root.right)
    print(root.data)
    postorderTraversal(root.left)
root = Node(1)

insert(root, Node(10))

insert(root, Node(5))

insert(root, Node(0))

insert(root, Node(3))

insert(root, Node(100))

#inorder traversal
inorderTraversal(root)

#post order traversal
postorderTraversal(root)

#pre order traversal

