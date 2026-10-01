import math

def get_student_info(stdscr):
    stdscr.addstr("  ID: ")
    s_id = stdscr.getstr().decode('utf-8')
    stdscr.addstr("  Name: ")
    name = stdscr.getstr().decode('utf-8')
    stdscr.addstr("  Date of Birth (DD/MM/YYYY): ")
    dob = stdscr.getstr().decode('utf-8')
    return s_id, name, dob

def get_course_info(stdscr):
    stdscr.addstr("  ID: ")
    c_id = stdscr.getstr().decode('utf-8')
    stdscr.addstr("  Name: ")
    name = stdscr.getstr().decode('utf-8')
    stdscr.addstr("  Credits (Trọng số): ")
    credits = int(stdscr.getstr().decode('utf-8'))
    return c_id, name, credits

def get_mark(stdscr, student_name, student_id):
    stdscr.addstr(f"  Mark for {student_name} (ID: {student_id}): ")
    raw_mark = float(stdscr.getstr().decode('utf-8'))
    return math.floor(raw_mark * 10) / 10