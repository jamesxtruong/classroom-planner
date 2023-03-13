#main.py
from classroom import Classroom 

#James Truong   CS302	    3-12-2023
#Program 4/5	Classroom Planner Program

""" 
This is the client test application. The software will be tested
through a series of calls from a menu interface. The application will
allow for schedule and planning of classrooms. The different types of 
classrooms are computer lab, lecture, and remote. 
"""

def main():
    print("\nWelcome to the Classroom Planner Program!\n")

    a_class = Classroom(1, 5, "The Base Class", "Basic Tech", True)
    b_class = Classroom()
    #a_class = Classroom(1, 5, "The Base Class", "Basic Tech", False)
    #print(a_class.print_info()) #returns None at end 
    a_class.print_info()
    b_class.print_info()


if __name__ == "__main__":
    main()