#test_classroom.py
import classroom 
from classroom import Classroom, Computer_lab, Lecture, Remote

# James Truong   CS302   3-13-2023
# Program 4/5    Classroom Planner Program 
# This is the testing suite where class testing of the classrooms will take place.
# This testing framework includes creating classrooms and using the classroom methods. 

# Classroom testing 
def test__default_classroom(): # Function to test default classroom object
    a = Classroom()
    assert a._occupants == 0
    assert a._capacity == 0
    assert a._special_notes == "none"
    assert a._technology == "n/a"
    assert a._ada == True 
    assert a._computers == 1
    assert a._projector == 1

def test_param_classroom():     # Function to test parameterized classroom object
    a = Classroom(5, 75, "moveable tables", "power outlets", True, 5, 0)
    assert a._occupants == 5
    assert a._capacity == 75
    assert a._special_notes == "moveable tables"
    assert a._technology == "power outlets"
    assert a._ada == True 
    assert a._computers == 5
    assert a._projector == 0

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

