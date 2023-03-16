# tables.py
from classroom import Classroom, Computer_lab, Lecture, Remote
import numpy as np 
import random 
# James Truong   CS302   3-15-2023
# Program 4/5    Classroom Planner Program 

"""
This file contains the class interface(s). To store and schedule
classes. 
"""
# Table
class Table:
    def __init__(self):
        # Array of linked lists 
        #self._classrooms = np.empty(5, dtype=object)
        #for i in range(5):
            #self.classrooms[i] = []

        # Randomize classrooms in each index
        #classroom_types = [Computer_lab, Lecture, Remote]
        pass
    pass
# AVL Tree to schedule and check classes
class Tree:
    def __init__(self):
        self._root = None
        pass
    def insert(self):
        pass
    def display(self):
        pass
    pass
# AVL Tree node
class Node:
    def __init__(self, key, value):
        self._key = key 
        self._value = value 
        self._left = None
        self._right = None
        self._height = 1
        pass
    pass
