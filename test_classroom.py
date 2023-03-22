#test_classroom.py
import classroom 
from classroom import Classroom, Computer_lab, Lecture, Remote

# James Truong   CS302   3-22-2023
# Program 4/5    Classroom Planner Program 

"""
This is the testing suite where class testing of the classrooms will take place.
This testing framework includes creating classrooms and using the classroom methods
for black box testing.  
"""

# Classroom testing 
def test_default_classroom(): # Function to test default classroom object
    a = Classroom()
    assert a._room_num == "---"
    assert a._occupants == 0
    assert a._capacity == 0
    assert a._special_notes == "none"
    assert a._technology == "n/a"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1
    assert a._booked == False

def test_param_classroom():     # Function to test parameterized classroom object
    a = Classroom("FAB 123", 5, 75, "moveable tables", "power outlets", True, 5, 0, True)
    assert a._room_num == "FAB 123"
    assert a._occupants == 5
    assert a._capacity == 75
    assert a._special_notes == "moveable tables"
    assert a._technology == "power outlets"
    assert a._ada == True 
    assert a._computers == 5
    assert a._projector == 0
    assert a._booked == True

def test_change_room_num_classroom():   # Function to test change room num method Classroom
    a = Classroom()
    a.change_room_num("FAB 140")
    assert a._room_num == "FAB 140"
    
def test_change_occupants_classroom():  # Function to test change occupants method Classroom
    a = Classroom()
    a.change_occupants(5)
    assert a._occupants == 5
    # test negative, non-integer (IMPLEMENT)

def test_change_capacity_classroom():   # Function to test change capacity method Classroom
    a = Classroom()
    a.change_capacity(15)
    assert a._capacity == 15
    # test negative, non-integer (IMPLEMENT)

def test_change_notes_classroom():      # Function to test changing special notes method
    a = Classroom()
    a.change_notes("New note")
    assert a._special_notes == "New note"

def test_change_tech_classroom():       # Function to test change technology notes method
    a = Classroom()
    a.change_tech("Has projector")
    assert a._technology == "Has projector"

def test_change_ada_classroom():        # Function to test change ada status method
    a = Classroom()
    a.change_ada('y')
    assert a._ada == True
    a.change_ada('n')
    assert a._ada == False 
    # test for invalid inputs (IMPLEMENT)

def test_change_computers_classroom():  # Function to test change computers method
    a = Classroom()
    a.change_computers(50)
    assert a._computers == 50
    # test negative, non-integer (IMPLEMENT)

def test_change_projector_classroom():  # Function to test change projector method
    a = Classroom()
    a.change_projector(0)
    assert a._projector == 0
    # test negative, non-integer (IMPLEMENT)

def test_check_full_classroom():        # Fucntion to test check full method 
    a = Classroom("FAB 150", 5, 5)
    b = Classroom("FAB 170", 4, 7)
    #c = Classroom("FAB 200", 0, 0)
    assert a.check_full() == True
    assert b.check_full() == False 

def test_operators_classroom():         # Function to test overloaded relational operators
    a = Classroom("FAB 123", 5, 10)
    b = Classroom("FAB 456", 4, 10)
    c = Classroom("FAB ABC", 4, 10)
    assert not (a < b)            # a < b is False
    assert not (a <= b)           # a <= b is False
    assert a > b                # a > b is True
    assert a >= b               # a >= b is True
    assert b < a                # b < a is True
    assert b <= a               # b <= a is True
    assert not (b > a)            # b > a is False
    assert not (b >= a)           # b >= a is False 
    assert not (b < c)            # b < c is False
    assert b <= c               # b <= c is True 
    assert not (b > c)            # b > c is False
    assert b >= c               # b >= c is True
    assert not (c < b)            # c < b is False
    assert c <= b               # c <= b is True
    assert not (c > b)            # c > b is False
    assert c >= b               # c >= b is True

# Derived classroom testing within hierarchy: Available Classrooms - Computer_lab, Lecture, Remote

def test_default_computer_lab(): # Function to test default computer lab object 
    a = Computer_lab()
    assert a._room_num == "---"
    assert a._occupants == 0
    assert a._capacity == 0
    assert a._special_notes == "none"
    assert a._technology == "n/a"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1
    assert a._booked == False
    assert a._monitors == 1

def test_param_computer_lab():     # Function to test parameterized computer lab object
    a = Computer_lab("FAB 123", 5, 75, "moveable tables", "power outlets", True, 5, 0, True, 5)
    assert a._room_num == "FAB 123"
    assert a._occupants == 5
    assert a._capacity == 75
    assert a._special_notes == "moveable tables"
    assert a._technology == "power outlets"
    assert a._ada == True 
    assert a._computers == 5
    assert a._projector == 0
    assert a._booked == True
    assert a._monitors == 5

def test_change_monitors_computer_lab():         # Function to test change monitor Computer_lab method
    a = Computer_lab()
    a.change_monitors(10)
    assert a._monitors == 10

def test_change_room_num_computer_lab():   # Function to test change room num method Computer lab
    a = Computer_lab()
    a.change_room_num("FAB 140")
    assert a._room_num == "FAB 140"
    
def test_change_occupants_computer_lab():  # Function to test change occupants method Computer lab
    a = Computer_lab()
    a.change_occupants(5)
    assert a._occupants == 5
    # test negative, non-integer (IMPLEMENT)

def test_change_capacity_computer_lab():   # Function to test change capacity method Computer lab
    a = Computer_lab()
    a.change_capacity(15)
    assert a._capacity == 15
    # test negative, non-integer (IMPLEMENT)

def test_change_notes_computer_lab():      # Function to test changing special notes method
    a = Computer_lab()
    a.change_notes("New note")
    assert a._special_notes == "New note"

def test_change_tech_computer_lab():       # Function to test change technology notes method
    a = Computer_lab()
    a.change_tech("Has projector")
    assert a._technology == "Has projector"

def test_change_ada_computer_lab():        # Function to test change ada status method
    a = Computer_lab()
    a.change_ada('y')
    assert a._ada == True
    a.change_ada('n')
    assert a._ada == False 
    # test for invalid inputs (IMPLEMENT)

def test_change_computers_computer_lab():  # Function to test change computers method
    a = Computer_lab()
    a.change_computers(50)
    assert a._computers == 50
    # test negative, non-integer (IMPLEMENT)

def test_change_projector_computer_lab():  # Function to test change projector method
    a = Computer_lab()
    a.change_projector(0)
    assert a._projector == 0
    # test negative, non-integer (IMPLEMENT)

def test_check_full_computer_lab():        # Fucntion to test check full method 
    a = Computer_lab("FAB 150", 5, 5)
    b = Computer_lab("FAB 170", 4, 7)
    #c = Classroom("FAB 200", 0, 0)
    assert a.check_full() == True
    assert b.check_full() == False 

def test_operators_classroom():         # Function to test overloaded relational operators
    a = Computer_lab("FAB 123", 5, 10)
    b = Computer_lab("FAB 456", 4, 10)
    c = Computer_lab("FAB ABC", 4, 10)
    assert not (a < b)              # a < b is False
    assert not (a <= b)             # a <= b is False
    assert a > b                    # a > b is True
    assert a >= b                   # a >= b is True
    assert b < a                    # b < a is True
    assert b <= a                   # b <= a is True
    assert not (b > a)              # b > a is False
    assert not (b >= a)             # b >= a is False 
    assert not (b < c)              # b < c is False
    assert b <= c                   # b <= c is True 
    assert not (b > c)              # b > c is False
    assert b >= c                   # b >= c is True
    assert not (c < b)              # c < b is False
    assert c <= b                   # c <= b is True
    assert not (c > b)              # c > b is False
    assert c >= b                   # c >= b is True

def test_default_lecture(): # Function to test default lecture object 
    a = Lecture()
    assert a._room_num == "---"
    assert a._occupants == 0
    assert a._capacity == 0
    assert a._special_notes == "none"
    assert a._technology == "n/a"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1
    assert a._booked == False
    assert a._podium == 1

def test_param_lecture():     # Function to test parameterized lecture  object
    a = Lecture("FAB 123", 5, 75, "moveable chairs and tables", "projector", True, 1, 1, True, 2)
    assert a._room_num == "FAB 123"
    assert a._occupants == 5
    assert a._capacity == 75
    assert a._special_notes == "moveable chairs and tables"
    assert a._technology == "projector"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1
    assert a._booked == True
    assert a._podium == 2

def test_change_podium():
    a = Lecture()
    b = Lecture()
    a.change_podium(3)
    assert a._podium == 3
    b.change_podium(-1)
    assert b._podium == 1
    a.change_podium(0)
    assert a._podium == 0

def test_default_remote(): # Function to test default remote object 
    a = Remote()
    assert a._room_num == "---"
    assert a._occupants == 0
    assert a._capacity == 0
    assert a._special_notes == "none"
    assert a._technology == "n/a"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1
    assert a._booked == False
    assert a._webcams == 1
    assert a._microphones == 1

def test_param_remote():     # Function to test parameterized remote  object
    a = Remote("FAB 300", 5, 55, "remote meetings", "has webcams", True, 2, 1, True, 2, 3)
    assert a._room_num == "FAB 300"
    assert a._occupants == 5
    assert a._capacity == 55
    assert a._special_notes == "remote meetings"
    assert a._technology == "has webcams"
    assert a._ada == True 
    assert a._computers == 2
    assert a._projector == 1
    assert a._booked == True
    assert a._webcams == 2
    assert a._microphones == 3 

def test_change_webcams():  # Function to test remote classroom method to change webcam 
    a = Remote()
    b = Remote()
    a.change_webcams(5)
    assert a._webcams == 5 
    b.change_webcams(-1)        # No change, invalid 
    assert b._webcams == 1 
    b.change_webcams(0)
    assert b._webcams == 0 

def test_change_microphones():  # Function to test remote classroom method to change microphones
    a = Remote()
    b = Remote()
    a.change_microphones(3)
    assert a._microphones == 3 
    b.change_microphones(-2)    # No change invalid 
    assert b._microphones == 1
    b.change_microphones(0)
    assert b._microphones == 0 

def test_operators_all_classroom():         # Function to test overloaded relational operators
    a = Computer_lab("FAB 300", 5, 10)
    b = Lecture("FAB 200", 4, 10)
    c = Remote("FAB 100", 4, 10)
    assert not (a < b)              # a < b is False
    assert not (a <= b)             # a <= b is False
    assert a > b                    # a > b is True
    assert a >= b                   # a >= b is True
    assert b < a                    # b < a is True
    assert b <= a                   # b <= a is True
    assert not (b > a)              # b > a is False
    assert not (b >= a)             # b >= a is False 
    assert not (b < c)              # b < c is False
    assert b <= c                   # b <= c is True 
    assert not (b > c)              # b > c is False
    assert b >= c                   # b >= c is True
    assert not (c < b)              # c < b is False
    assert c <= b                   # c <= b is True
    assert not (c > b)              # c > b is False
    assert c >= b                   # c >= b is True

# Data structure test suite create, insert, remove (TO IMPLEMENT)...