# classroom.py
import numpy as np 
import os 
# James Truong   CS302   3-22-2023
# Program 4/5    Classroom Planner Program 

"""
This is the file that contains the class interface(s).
There is a base class called classroom and it's subclasses are
different types of classes such as: computer lab, lecture, and remote.
"""
class Classroom:                # Base class 
    def __init__(self, room_num = "---", occupants = 0, capacity = 0, special_notes = "none", technology = "n/a",
                 ada = True, computers = 1, projector = 1, booked = False):                   # Default constructor
        self._room_num = room_num              # Room number of class
        self._occupants = occupants             # Number of occupants in class
        self._capacity = capacity               # Capacity of classroom for occupants
        self._special_notes = special_notes     # Special notes for classroom
        self._technology = technology           # Technology info for classroom 
        self._ada = ada                         # ADA accessible classroom 
        self._computers = computers             # By default every classroom has a computer 
        self._projector = projector             # By default every classroom has a projector 
        self._booked = booked                   # By default every classroom is not booked 

    def print_info(self):        # Print information about classroom
        print("Classroom info: ")     # Print header
        print(f"Room number: {self._room_num}")             # Room num / name
        print(f"Occupants: {self._occupants} / Capacity: {self._capacity}") # Occupants / capacity
        #print(f"Capacity: {self._capacity}")
        print(f"Special Notes: {self._special_notes}")      # Special classroom notes
        print(f"Technology info: {self._technology}")       # Technology notes
        if self._ada:                                       # ada status
            print("ADA Accessible: Yes")
        else:
            print("ADA Accessible: No")
        print(f"Computers: {self._computers}")              # Number of computers
        print(f"Projector: {self._projector}")              # Number of projectors
        #print(f"Booked: {self._booked}")
        if self._booked:                                    # Booked status 
            print("Booked: Yes")
        else:
            print("Booked: No")
        return None
        #pass 
    
    def change_room_num(self, room_num = None):
        if room_num is None:
            room_num = input("Enter a room number for the classroom: ")
        self._room_num = room_num

    def change_occupants(self, occupants = None):   # Change number of occupants in class
        if occupants is None:
            occupants = int(input("Enter the number of occupants: "))
        self._occupants = occupants
        #pass 

    def change_capacity(self, capacity = None):     # Change classroom capacity 
        if capacity is None:
            capacity = int(input("Enter the classroom's capacity: "))
        self._capacity = capacity
        #pass

    def change_notes(self, special_notes = None):   # Change special notes for classroom
        if special_notes is None:
            special_notes = input("Enter special notes for the classroom: ")
        self._special_notes = special_notes 
        #pass

    def change_tech(self, technology = None):       # Change technology description
        if technology is None:
            technology = input("Enter the technology available for the classroom: ")
        self._technology = technology 
        #pass

    def change_ada(self, ada = None):               # Change ada status of classroom
        if ada is None:
            ada = input("Enter classroom ADA compliant status: y/n: ")
            if input.lower() == 'y':
                self._ada = True
            elif input.lower() == 'n':
                self._ada = False
        if ada.lower() == 'y':
            self._ada = True
        elif ada.lower() == 'n':
            self._ada = False
        #self._ada = ada
        #pass 
    def change_computers(self, computers = None):   # Change number of computers in classroom
        if computers is None:
            computers = input("Enter the number of computers available for the classroom: ")
        self._computers = computers

    def change_projector(self, projector = None):   # Change number of projectors in classroom 
        if projector is None:
            projector = input("Enter the amount of projectors available for the classroom: ")
        self._projector = projector

    def check_full(self):                       # Check if classroom is full
        return self._occupants == self._capacity 

    # Operator overloading to compare availablility (occupants to capacity)
    def __lt__(self, op2):                      # Less occupants than classroom capacity allowed
        return self._occupants < op2._occupants 

    def __le__(self, op2):                      # Less than or equal to occupants to class capacity
        return self._occupants <= op2._occupants  

    def __gt__(self, op2):                      # Greater than classroom capacity allowed
        return self._occupants > op2._occupants    

    def __ge__(self, op2):                      # Greater than or equal to occupants to class capacity 
        return self._occupants >= op2._occupants 
    
    #def __add__(self, to_add):
        #if self.occupants + to_add <= self.capacity:
            #self.occupants += add
        #else

        #return self.

    #def __sub__

class Computer_lab(Classroom):  # Computer lab sub-class, is a Classroom 
    #def __init__(self):
    def __init__(self, room_num = "---", occupants = 0, capacity = 0, special_notes = "none", technology = "n/a",
                 ada = True, computers = 1, projector = 1, booked = False, monitors = 1):  
        super().__init__(room_num, occupants, capacity, special_notes, technology, ada, computers, projector, booked)
        self._monitors = monitors

    def print_info(self):
        super().print_info()    # Call base class print method 
        print(f"Monitors: {self._monitors}")
        return None

    def change_monitors(self, monitors = None):
        if monitors is None:
            monitors = input("Enter the number of monitors available for the classroom: ")
        self._monitors = monitors
        #pass

class Lecture(Classroom):       # Lecture is a sub-class, is a Classroom
    #def __init__(self):
    def __init__(self, room_num = "---", occupants = 0, capacity = 0, special_notes = "none", technology = "n/a",
                 ada = True, computers = 1, projector = 1, booked = False, podium = 1):  
        super().__init__(room_num, occupants, capacity, special_notes, technology, ada, computers, projector, booked)
        self._podium = podium

    def print_info(self):
        super().print_info()    # Call base class print method 
        print(f"Podium: {self._podium}")
        return None
        #pass
    
    def change_podium(self, podium = None):
        if podium is None:
            podium = input("Enter the number of podiums available for the classroom: ")
        if podium < 0:
            print("Invalid number")
        elif podium >= 0:
            self._podium = podium 

class Remote(Classroom):        # Remote is a sub-class, is a Classroom 
    #def __init__(self):
    def __init__(self, room_num = "---", occupants = 0, capacity = 0, special_notes = "none", technology = "n/a",
                 ada = True, computers = 1, projector = 1, booked = False, webcams = 1, microphones = 1):  
        super().__init__(room_num, occupants, capacity, special_notes, technology, ada, computers, projector, booked)
        self._webcams = webcams
        self._microphones = microphones

    def print_info(self):
        super().print_info()    # Call base class print method 
        print(f"Webcams: {self._webcams}")
        print(f"Microphones: {self._microphones}")
        return None
        #pass 

    def change_webcams(self, webcams = None):
        if webcams is None:
            webcams = input("Enter the number of webcams available for the classroom: ")
        if webcams < 0:
            print("Invalid size")
        elif webcams >= 0:
            self._webcams = webcams

    def change_microphones(self, microphones = None):
        if microphones is None:
            microphones = input("Enter the number of microphones available for the classroom: ")
        if microphones < 0:
            print("Invalid size")
        elif microphones >= 0:
            self._microphones = microphones 
        #pass 
    
   