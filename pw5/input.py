import curses
from datetime import datetime

def get_student_info(stdscr):
    stdscr.addstr("Enter Student ID: ")
    s_id = stdscr.getstr().decode('utf-8')
    
    stdscr.addstr("Enter Student Name: ")
    name = stdscr.getstr().decode('utf-8')
    
   
    while True:
        stdscr.addstr("Enter DoB (DD/MM/YYYY): ")
        dob = stdscr.getstr().decode('utf-8')
        try:
            datetime.strptime(dob, "%d/%m/%Y")
            break
        except ValueError:
            stdscr.addstr("Invalid format! Please try again (e.g., 31/03/2006).\n")
            
    return s_id, name, dob


def get_course_info(stdscr):
    stdscr.addstr("Enter Course ID: ")
    c_id = stdscr.getstr().decode('utf-8')
    
    stdscr.addstr("Enter Course Name: ")
    name = stdscr.getstr().decode('utf-8')
    
    
    while True:
        stdscr.addstr("Enter Course Credits (number): ")
        credits_str = stdscr.getstr().decode('utf-8')
        if credits_str.isdigit() and int(credits_str) > 0:
            credits = int(credits_str)
            break
        else:
            stdscr.addstr("Invalid credits! Must be a positive integer.\n")
            
    return c_id, name, credits


def get_mark(stdscr, student_name, student_id):
    
    while True:
        stdscr.addstr(f"Enter mark for {student_name} (ID: {student_id}): ")
        mark_str = stdscr.getstr().decode('utf-8')
        try:
            mark = float(mark_str)
            if 0 <= mark <= 20: 
                return mark
            else:
                stdscr.addstr("Mark must be between 0 and 20. Try again.\n")
        except ValueError:
            stdscr.addstr("Invalid input! Please enter a number.\n")