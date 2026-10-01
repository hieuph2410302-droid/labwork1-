import curses
import numpy as np
import input as inp
import output as out
from domains import Student, Course

class ManagementSystem:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter number of students in the class: ")
        num = int(self.stdscr.getstr().decode('utf-8'))
        for i in range(num):
            self.stdscr.addstr(f"\nStudent {i+1}:\n")
            s_id, name, dob = inp.get_student_info(self.stdscr)
            self.students.append(Student(s_id, name, dob))

    def input_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter number of courses: ")
        num = int(self.stdscr.getstr().decode('utf-8'))
        for i in range(num):
            self.stdscr.addstr(f"\nCourse {i+1}:\n")
            c_id, name, credits = inp.get_course_info(self.stdscr)
            self.courses.append(Course(c_id, name, credits))

    def input_marks(self):
        self.stdscr.clear()
        if not self.courses or not self.students:
            self.stdscr.addstr("Please input students and courses first!\nPress any key...")
            self.stdscr.getch()
            return
        
        out.display_courses(self.stdscr, self.courses, pause=False)
        self.stdscr.addstr("\nSelect a course ID to input marks: ")
        course_id = self.stdscr.getstr().decode('utf-8')
        
        if not any(c.get_id() == course_id for c in self.courses):
            self.stdscr.addstr("Course not found!\nPress any key...")
            self.stdscr.getch()
            return

        if course_id not in self.marks:
            self.marks[course_id] = {}

        self.stdscr.addstr(f"\nEntering marks for course '{course_id}':\n")
        for student in self.students:
            mark = inp.get_mark(self.stdscr, student.get_name(), student.get_id())
            self.marks[course_id][student.get_id()] = mark
            
        self.calculate_gpa()

    def calculate_gpa(self):
        for student in self.students:
            s_marks = []
            s_credits = []
            for course in self.courses:
                c_id = course.get_id()
                if c_id in self.marks and student.get_id() in self.marks[c_id]:
                    s_marks.append(self.marks[c_id][student.get_id()])
                    s_credits.append(course.get_credits())
            
            if s_credits:
                arr_marks = np.array(s_marks)
                arr_credits = np.array(s_credits)
                gpa = np.average(arr_marks, weights=arr_credits)
                student.set_gpa(gpa)

        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def show_student_marks(self):
        self.stdscr.clear()
        if not self.marks:
            self.stdscr.addstr("No marks have been inputted yet.\nPress any key...")
            self.stdscr.getch()
            return
            
        out.display_courses(self.stdscr, self.courses, pause=False)
        self.stdscr.addstr("\nSelect a course ID to view marks: ")
        course_id = self.stdscr.getstr().decode('utf-8')
        
        if course_id not in self.marks:
            self.stdscr.addstr("No marks available for this course.\nPress any key...")
            self.stdscr.getch()
            return
            
        out.display_marks(self.stdscr, self.marks, self.courses, self.students, course_id)

    def run(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("==============================\n")
            self.stdscr.addstr("  STUDENT MARK MANAGEMENT (PW4)\n")
            self.stdscr.addstr("==============================\n")
            self.stdscr.addstr("1. Input students\n")
            self.stdscr.addstr("2. Input courses\n")
            self.stdscr.addstr("3. Input marks\n")
            self.stdscr.addstr("4. List students\n")
            self.stdscr.addstr("5. List courses\n")
            self.stdscr.addstr("6. Show marks\n")
            self.stdscr.addstr("0. Exit\n")
            self.stdscr.addstr("\nEnter your choice (0-6): ")
            
            choice = self.stdscr.getstr().decode('utf-8')
            
            if choice == '1': self.input_students()
            elif choice == '2': self.input_courses()
            elif choice == '3': self.input_marks()
            elif choice == '4': out.display_students(self.stdscr, self.students)
            elif choice == '5': out.display_courses(self.stdscr, self.courses)
            elif choice == '6': self.show_student_marks()
            elif choice == '0': break

def main(stdscr):
    app = ManagementSystem(stdscr)
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)