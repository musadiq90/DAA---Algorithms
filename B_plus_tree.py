# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:35:26 2019

@author: MUSADIQ.4683179
"""

from datetime import datetime
start = datetime.now()
class Node(object):
    
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []
        self.leaf = True

    def add(self, key, value):
        if not self.keys:
            self.keys.append(key)
            self.values.append([value])
            return None
        for i, item in enumerate(self.keys):
            if key == item:
                self.values[i].append(value)
                break
            elif key < item:
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                self.values = self.values[:i] + [[value]] + self.values[i:]
                break
            elif i + 1 == len(self.keys):
                self.keys.append(key)
                self.values.append([value])
                break

    def split(self):
        left = Node(self.order)
        right = Node(self.order)
        mid = self.order / 2
        left.keys = self.keys[:int(mid)]
        left.values = self.values[:int(mid)]
        right.keys = self.keys[int(mid):]
        right.values = self.values[int(mid):]
        self.keys = [right.keys[0]]
        self.values = [left, right]
        self.leaf = False

    def is_full(self):
        return len(self.keys) == self.order

    def show(self, counter=0):
        print(counter, str(self.keys))
        if not self.leaf:
            for item in self.values:
                item.show(counter + 1)

class BPlusTree(object):
    def __init__(self, order=8):
        self.root = Node(order)

    def _find(self, node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i
        return node.values[i + 1], i + 1
   
    def _merge(self, parent, child, index):
        parent.values.pop(index)
        pivot = child.keys[0]
        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.values = parent.values[:i] + child.values + parent.values[i:]
                break
            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.values += child.values
                break
 
    def insert(self, key, value):
        parent = None
        child = self.root
        while not child.leaf:
            parent = child
            child, index = self._find(child, key)
        child.add(key, value)
        if child.is_full():
            child.split()
            if parent and not parent.is_full():
                self._merge(parent, child, index)

    def retrieve(self, key):
        child = self.root
        while not child.leaf:
            child, index = self._find(child, key)
        for i, item in enumerate(child.keys):
            if key == item:
                return child.values[i]
        return None

    def show(self):
        self.root.show()




def B_plus_tree():
    
    input_values = input("enter the number of values you want to enter (Must be greater than 4 ): ")
    
    
    print('Initializing B+ tree...')
    
    bplustree = BPlusTree(order=4)
    n = int(input_values)
    
    for i in range(0,n):
        insert_key = input("Enter the key:  ")
        insert_value = input("Enter the value:  ")
        bplustree.insert(insert_key, insert_value)
        bplustree.show()
   
    print("\n Values inserted: ")
    show = input("\n Enter the key from the list to print the value: ")
    print(bplustree.retrieve(show))
    print("\n enter the value you want to delete") 

if __name__ == '__main__':
    start = datetime.now()  
    print("The tree has been displayed using the the list.\n")
    print("0 ['3'] \n1 ['1', '2'] \n1 ['3', '4', '5'] \n")
    print("Here 0 and 1 are the levels of the tree and the keys are the nodes value ")
    print('\n')
    B_plus_tree()
    end = datetime.now()
    print("\n \n")    
    print("Program started at: ", start)
    print("\nProgram ended at: ", end)
    time = end - start   
    print("\n \n total time take is: ", time)
