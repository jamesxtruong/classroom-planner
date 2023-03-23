# main.py
from classroom import Classroom, Computer_lab, Lecture, Remote
from tables import Linked_list
import numpy as np 
# James Truong   CS302	    3-22-2023
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

    my_classes = Linked_list()

    # Menu loop interface, IN PROGRESS
    while not choice.isalpha() or choice.lower() != 'd':
        print("\nClassroom menu: ")
        print("(a) Add Classroom \t (b) Display Classroom \t\t (_) Remove Classrooms \t\t (d) Exit")

        choice = input("Select an option: ")

        if choice.lower() == 'a':     # Add classroom 
            print("\nSELECTED: Add Classroom")
            print("(1) Add Computer Lab \t (2) Add Lecture \t\t (3) Add Remote")
            option = int(input("Enter an integer option: "))

            if option == 1:
                #a = Computer_lab()  # Default constructor computer lab
                room_num = input("Enter the name/room number for the computer lab (ex. FAB 340): ")
                occupants = int(input("Enter the number of occupants for the computer lab: "))
                capacity = int(input("Enter the max capacity for the computer lab: "))
                special_notes = input("Enter special notes for the computer lab: ")
                technology = input("Enter technology decsription for the computer lab: ")
                ada = True # By default all classrooms are ada accessible 
                computers = int(input("Enter the number of computers in the computer lab: "))
                projector = int(input("Enter the number of projectors in the computer lab: "))
                booked = True 
                monitors = int(input("Enter the number of monitors in the computer lab: "))
                a = Computer_lab(room_num, occupants, capacity, special_notes, technology, ada, computers, 
                    projector, booked, monitors)

                my_classes.insert(a)

            elif option == 2:
                #b = Lecture()
                room_num = input("Enter the name/room number for the lecture room (ex. FAB 340): ")
                occupants = int(input("Enter the number of occupants for the lecture room: "))
                capacity = int(input("Enter the max capacity for the lecture room: "))
                special_notes = input("Enter special notes for the lecture room: ")
                technology = input("Enter technology decsription for the lecture room: ")
                ada = True # By default all classrooms are ada accessible 
                computers = int(input("Enter the number of computers in the lecture room: "))
                projector = int(input("Enter the number of projectors in the lecture room: "))
                booked = True
                podium = int(input("Enter the number of podiums in the lecture room: "))
                b = Lecture(room_num, occupants, capacity, special_notes, technology, ada, computers, 
                    projector, booked, podium)

                my_classes.insert(b)

            elif option == 3:
                #c = Remote()
                room_num = input("Enter the name/room number for the remote room (ex. FAB 340): ")
                occupants = int(input("Enter the number of occupants for the remote room: "))
                capacity = int(input("Enter the max capacity for the remote room: "))
                special_notes = input("Enter special notes for the remote room: ")
                technology = input("Enter technology decsription for the remote room: ")
                ada = True # By default all classrooms are ada accessible 
                computers = int(input("Enter the number of computers in the remote room: "))
                projector = int(input("Enter the number of projectors in the remote room: "))
                booked = True
                webcams = int(input("Enter the number of webcams in the remote room: "))
                microphones = int(input("Enter the number of microphones in the remote room: "))
                c = Remote(room_num, occupants, capacity, special_notes, technology, ada, computers, 
                    projector, booked, webcams, microphones)
                
                my_classes.insert(c)

        elif choice.lower() == 'b':   # Display classroom
            print("\nSELECTED: Display Classrooms\n")
            if my_classes is not None:   # List of classrooms display 
                my_classes.display() 
            """""
            print("\nRecently added...")
            if a is not None:
                print("\n<< COMPUTER LABS >>")          # Print computer lab classroom
                a.print_info()
            else:
                print("\nComputer lab classroom has not been created \n")
            if b is not None:
                print("\n<< LECTURE >>")                # Print lecture classroom
                b.print_info()
            else:
                print("\nLecture classroom has not been created \n")
            if c is not None:
                print("\n<< REMOTE >>")                 # Print remote classroom 
                c.print_info()
            else:
                print("\nRemote classroom has not been created \n")
            """
        #elif choice.lower() == '_':   # Exit classroom menu
            #print("\nSELECTED: Remove Classrooms")
            #my_classes.remove_all 

        elif choice.lower() == 'd':   # Exit classroom menu
            print("\nSELECTED: Exit")
            print("... Exiting the menu")
    # Create Classroom objects 
    #a_class = Classroom("FAB 000", 1, 5, "The Base Class", "Basic Tech", True) # Parameterized base class
    #b_class = Classroom()       # Default base class classroom
    #c_class = Computer_lab()    # Sub class computer lab classroom
    #d_class = Lecture()         # Sub class lecture classroom
    #e_class = Remote()          # Sub class remote classroom

    #a_class = Classroom(1, 5, "The Base Class", "Basic Tech", False)
    #print(a_class.print_info()) #returns None at end 

    # Print Classrooms 
    #a_class.print_info()        # Parameterized object
    #b_class.print_info()        # Default parameter object
    #c_class.print_info()        # Default parameter object (computer lab)
    #d_class.print_info()        # Default parameter object (lecture)
    #e_class.print_info()        # Default parameter object (remote)


if __name__ == "__main__":
    main()