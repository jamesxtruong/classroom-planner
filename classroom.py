#classroom.py

#James Truong   CS302   3-12-2023
#Program 4/5    Classroom Planner Program 

"""
This is the file that contains the class interface(s).
There is a base class called classroom and it's subclasses are
different types of classes such as: computer lab, lecture, and remote.
"""
class Classroom:                #Base class 
    def __init__(self, occupants = 0, capacity = 0, special_notes = "", technology = "",
                 ada = True):    #Default constructor
        self._occupants = occupants         #Number of occupants in class
        self._capacity = capacity           #Capacity of classroom for occupants
        self._special_notes = special_notes #Special notes for classroom
        self._technology = technology       #Technology info for classroom
        self._ada = ada                     #ADA accessible classroom 

    def print_info(self):        #Print information about classroom
        print("\nClassroom info: \n")
        print(f"Occupants: {self._occupants} | Capacity: {self._capacity}")
        #print(f"Capacity: {self._capacity}")
        print(f"Special Notes: {self._special_notes}")
        print(f"Technology info: {self._technology}")
        if(self._ada):
            print("ADA Accessible: Yes")
        else:
            print("ADA Accessible: No")
        return None
        #pass 
    def change_occupants(self, occupants = None):
        pass 
    def change_capacity(self, capacity = None):
        pass
    def change_notes(self, special_notes = None): 
        pass
    def change_tech(self, technology = None): 
        pass
    def change_ada(self, ada = None):
        pass 

class Computer_lab(Classroom):  #Computer lab sub-class, is a Classroom 
    pass
class Lecture(Classroom):       #Lecture is a sub-class, is a Classroom
    pass
class Remote(Classroom):        #Remote is a sub-class, is a Classroom 
    pass 
