# main.py
from classroom import Classroom, Computer_lab, Lecture, Remote
from tables import Table, Tree 
import numpy as np 
# James Truong   CS302	    3-15-2023
# Program 4/5	Classroom Planner Program

""" 
This is the client test application. The software will be tested
through a series of calls from a menu interface. The application will
allow for schedule and planning of classrooms. The different types of 
classrooms are computer lab, lecture, and remote. 
"""

def main():
    # Welcome Message
    print("\nWelcome to the Classroom Planner Program!")

    choice = ''             # Main classroom menu option
    a = None
    b = None
    c = None

    # Menu loop interface, IN PROGRESS
    while not choice.isalpha() or choice.lower() != 'c':
        print("Classroom menu: ")
        print("(a) Add Classroom \t (b) Display Classroom \t (c) Exit")

        choice = input("Select an option: ")

        if choice.lower() == 'a':     # Add classroom 
            print("SELECTED: Add Classroom")
            print("(1) Add Computer Lab \t (2) Add Lecture \t (3) Add Remote")
            option = int(input("Enter an integer option: "))

            if option == 1:
                a = Computer_lab()  # Default constructor computer lab
                #occupants = int(input("Enter the number of occupants for the computer lab: "))
                #capacity = int(input("Enter the max capacity for the computer lab: "))
                #special_notes = input("Enter special notes for the computer lab: ")
                #technology = input("Enter technology decription for the computer lab: ")
                #ada = True # By default all classrooms are ada accessible 
                #computers = int(input("Enter the number of computers in the computer lab: "))
                #projector = int(input("Enter the number of projectors in the computer lab: "))
                #monitors = int(input("Enter the number of monitors in the computer lab: "))
                 #a = Computer_lab(occupants, capacity, special_notes, technology, ada, computers, 
                    #projector, monitors)
            elif option == 2:
                b = Lecture()
            elif option == 3:
                c = Remote()

        elif choice.lower() == 'b':   # Display classroom
            if a is not None:
                a.print_info()
            else:
                print("Computer lab classroom has not been created ")
            if b is not None:
                b.print_info()
            else:
                print("Lecture classroom has not been created ")
            if c is not None:
                c.print_info()
            else:
                print("Remote classroom has not been created ")

        elif choice.lower() == 'c':   # Exit classroom menu
            print("SELECTED: Exit")
            print("... Exiting the menu")

    # Create Classroom objects 
    a_class = Classroom("FAB 000", 1, 5, "The Base Class", "Basic Tech", True) # Parameterized base class
    b_class = Classroom()       # Default base class classroom
    c_class = Computer_lab()    # Sub class computer lab classroom
    d_class = Lecture()         # Sub class lecture classroom
    e_class = Remote()          # Sub class remote classroom

    #a_class = Classroom(1, 5, "The Base Class", "Basic Tech", False)
    #print(a_class.print_info()) #returns None at end 

    # Print Classrooms 
    a_class.print_info()        # Parameterized object
    b_class.print_info()        # Default parameter object
    c_class.print_info()        # Default parameter object (computer lab)
    d_class.print_info()        # Default parameter object (lecture)
    e_class.print_info()        # Default parameter object (remote)


if __name__ == "__main__":
    main()