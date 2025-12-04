# Classroom Planner Program

**Created by:** James Truong for CS302 Winter 2023
**Program:** #4/#5

---

## Overview

Welcome to the Classroom Planner Program!

This Python application helps manage and schedule classrooms for academic institutions. The program assists in matching classes to appropriate classrooms based on room features, capacity, and equipment requirements. The application supports three types of classrooms: computer labs, lecture rooms, and remote-enabled rooms. Each room has unique characteristics and capabilities.

The program uses a class hierarchy to organize different classroom types and implements custom data structures (array of linked lists and tree structures) to efficiently manage classroom inventory and class scheduling.

---

## How to Run

### Prerequisites

- Python 3.x
- NumPy library

### Installation

Install required dependencies:

```bash
pip install numpy pytest
```

### Execution

Run the main program:

```bash
python main.py
```

Run tests:

```bash
pytest test_classroom.py
```

---

## Usage

The program provides a menu-driven interface using letter inputs for navigation.

### Main Menu Options

- **(a) Add Classroom** - Create a new classroom (computer lab, lecture, or remote)
- **(b) Display Classroom** - View all classrooms in the system
- **(d) Exit** - Quit the program

When adding a classroom, you'll be prompted to enter specific information based on the room type. All classrooms are ADA accessible by default.

---

## Classroom Types

All classrooms share common attributes (room number, occupants, capacity, special notes, technology, ADA accessibility, computers, projectors, and booking status). Each type has unique equipment:

### Computer Lab

- **Computers** - Number of computers available
- **Monitors** - Number of monitors in the lab
- **Projector** - Projection equipment

Computer labs are designed for hands-on learning where each student has access to a workstation.

### Lecture Room

- **Computers** - Technology available
- **Podium** - Number of podiums for instructors
- **Projector** - Presentation equipment

Lecture rooms are traditional classroom spaces optimized for instructor-led teaching with overhead projection capabilities.

### Remote Room

- **Computers** - Available technology
- **Webcams** - Number of cameras for remote streaming
- **Microphones** - Audio equipment count
- **Projector** - Display equipment

Remote rooms are equipped for distance learning with cameras and microphones to support virtual attendance and hybrid learning environments.

---

## Project Structure

- `main.py` - Client application entry point with menu interface
- `classroom.py` - Classroom class hierarchy (Classroom, Computer_lab, Lecture, Remote)
- `tables.py` - Data structure implementations (Linked_list)
- `test_classroom.py` - PyTest test suite for unit testing

---

Happy scheduling!
