def display_courses(stdscr, courses, pause=True):
    stdscr.clear()
    stdscr.addstr("--- List of Courses ---\n")
    for c in courses:
        stdscr.addstr(f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}\n")
    if pause:
        stdscr.addstr("\nPress any key to continue...")
        stdscr.getch()

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr("--- List of Students (Sorted by GPA) ---\n")
    for s in students:
        stdscr.addstr(f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.1f}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.getch()

def display_marks(stdscr, marks, courses, students, course_id):
    stdscr.clear()
    stdscr.addstr(f"\n--- Marks for Course '{course_id}' ---\n")
    for student in students:
        s_id = student.get_id()
        if s_id in marks[course_id]:
            stdscr.addstr(f"  {student.get_name()}: {marks[course_id][s_id]}\n")
    stdscr.addstr("\nPress any key to continue...")
    stdscr.getch()