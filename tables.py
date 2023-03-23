# tables.py
from classroom import Classroom, Computer_lab, Lecture, Remote
import numpy as np 
import random 
# James Truong   CS302   3-22-2023
# Program 4/5    Classroom Planner Program 

"""
This file contains the class interface(s). To store available classrooms 
and schedule classrooms. The classrooms available to the user are preset in terms
of what classrooms are available. Classrooms can be displayed, added, and changed.
"""
#class Scheduler: # Class to contain menu interface and array of linked list of available classrooms and tree to schedule classrooms 
        #pass 

# Table (array of linked lists of random classrooms)
class Classroom_list:
    def __init__(self):      
        self._num_labs = 8        # 8 computer labs available to book
        self._num_remote = 6      # 6 remote classrooms available to book
        self._num_lecture = 20    # 20 lecture classrooms avaialble to book   
        self._array = []
        for i in range(4):     # Array of linked lists (Classrooms)
            self._array.append(Linked_list())

    #def setup_classrooms(self): # Function to create set amount of classrooms available 0
        #pass

# Linked list node of classroom
class Node: 
    def __init__(self, a_classroom, next = None):
        self._classroom = a_classroom 
        self._next = next

# Linked list class, list of classrooms
class Linked_list: 
    def __init__(self):
        self._head = None 

    def insert(self, a_classroom):  # Public wrapper
        new_node = Node(a_classroom)

        if self._head is None:      # Empty list, insert 
            self._head = new_node
        else:
            self._insert(new_node, self._head) # Recursive call

    def _insert(self, new_node, current): # Recursive function to insert
        if current._next is None:
            current._next = new_node
        else:
            self._insert(new_node, current._next)

    def remove_all(self):       # Function to remove whole list 
        self._head = None 

    def display(self):                  # Wrapper function to display classroom list
        self._display(self._head)

    def _display(self, current):        # Recursive function to display classroom list
        if current is not None:
            current._classroom.print_info()
            self._display(current._next) # Recursive call 

# 2-3 Tree to schedule and check classes (IN PROGRESS SWITCHING TO 2-3 IMPLEMENTATION...)
class Tree:
    def __init__(self):         
        self._root = None

    def insert(self, time, a_classroom):      # Public function insert 
        if self._root is None:              # Empty 
            self._root = Tree_node(time)
            self._root._classes._head = Node(a_classroom)
        else:
            self._insert(time, Classroom, self._root)

    def _insert(self, time, a_classroom, current):    # Private wrapper 
        if time == current._time:                   # Check if classroom (node) for time already exists 
            current._classes._head = Node(Classroom, current._classes._head)
        elif time < current._time:                  # Go the left is time is less than current
            if current._left is None: 
                current._left = Tree_node(time)
                current._left._clases._head = Node(a_classroom)
            else:
                self._insert(time, Classroom, current._left) # Recursive call traverse left
        else:                                       # Time is greater than current, go to right 
            if current._right is None:
                current._right = Tree_node(time)
                current._right._classes._head = Node(a_classroom)
            else:
                self._insert(time, a_classroom, current._right) # Recursive call traverse right

    def display(self):                      # Public wrapper display 
        self._display(self._root)           # Recursive function call to display
    
    def _display(self, current):            # Recursive function to display 
        if current is None:                 # Base case
            return 
        elif current is not None:
            self._display(current._left)    # Inorder traversal, go left first
            print(f"Class time: {current._time}") 
            temp = current._classes._head   # Temp pointer to head to traverse classes to print
            while temp is not None:         # Display 
                temp._classroom.print_info()
                temp = temp._next           # Iterate 
            self._display(current._right)   # Traverse right tree

    def remove_all(self):                    # Function to remove all classrooms scheduled in tree 
        self._root = None

# 2-3 Tree node
class Tree_node:
    def __init__(self, time):
        self._time_1 = time       # Two data in node 
        self._time_2 = None 
        self._classes_1 = Linked_list() # Linked of classrooms in Node 
        self._classes_2 = Linked_list()
        self._parent = None 
        self._left = None          # Left child
        self._middle = None        # Middle child
        self._right = None         # Right child
        #self._height = 1   
    

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
      