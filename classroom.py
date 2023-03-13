#classroom.py

#James Truong   CS302   3-12-2023
#Program 4/5    Classroom Planner Program 

#This is the file that contains the class interface(s).
#There is a base class called classroom and it's subclasses are
#different types of classes such as: computer lab, lecture, and remote.

class Classroom:
    def __init__(self)          #Default constructor
        self._capacity = 0
        self._occupants = 0
        self._special_notes = ""
        self._technology_capabilities = ""
        self._ada = True 
    def print_info(self)        #Print information about classroom

class Computer_lab(Classroom):
    pass
class Lecture(Classroom):
    pass
class Remote(Classroom):
    pass 
