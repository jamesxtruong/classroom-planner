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
# Table (array of linked lists of random classrooms)
class Table:
    def __init__(self):
        # Array of linked lists 
        #self._classrooms = np.empty(5, dtype=object)
        #for i in range(5):
            #self.classrooms[i] = []

        # Randomize classrooms in each index
        #classroom_types = [Computer_lab, Lecture, Remote]
        #for i in range(random.randint(5, 10)): #5 - 10 classes
            #class_type = random.choice(classroom_types)
            #occupants = 0
            #capacity = random.randint(20, 100)

            #if class_type == Computer_lab:
                #a_room = class_type()
                #computers = random.randint(10, 50)
                #a_room.change_capacity(capacity)
                #a_room.change_computers(computers)
            #elif class_type == Lecture:
                #a_room = class_type()
                #podiums = random.randint(1, 2)
                #a_room.change_capacity(capacity)
                #a_room.change_podiums(podiums)
            #elif class_type == Remote:
                #a_room = class_type()
                #microphones = random.randint(1, 3)
                #webcams = random.randint(1, 3)
                #a_room.change_capacity(capacity)
                #a_room.change_microphones(microphones)
                #a_room.change_webcames(webcams)
            #self._classrooms[random.randint(0, 4).append(a_room)]
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
