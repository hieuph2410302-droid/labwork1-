import math
import numpy as np
import curses

class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""
        self.__gpa = 0.0

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa

    def input(self, stdscr):
        stdscr.addstr("  ID: ")
        self.__id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Name: ")
        self.__name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Date of Birth (DD/MM/YYYY): ")
        self.__dob = stdscr.getstr().decode('utf-8')

    def list(self, stdscr):
        stdscr.addstr(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob} | GPA: {self.__gpa:.1f}\n")


class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0

    def get_id(self): return self.__id
    def get_credits(self): return self.__credits

    def input(self, stdscr):
        stdscr.addstr("  ID: ")
        self.__id = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Name: ")
        self.__name = stdscr.getstr().decode('utf-8')
        stdscr.addstr("  Credits (Trọng số): ")
        self.__credits = int(stdscr.getstr().decode('utf-8'))

    def list(self, stdscr):
        stdscr.addstr(f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}\n")


class ManagementSystem:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter number of students in the class: ")
        num = int(self.stdscr.getstr().decode('utf-8'))
        for i in range(num):
            self.stdscr.addstr(f"\nStudent {i+1}:\n")
            student = Student()
            student.input(self.stdscr)
            self.__students.append(student)

    def input_courses(self):
        self.stdscr.clear()
        self.stdscr.addstr("Enter number of courses: ")
        num = int(self.stdscr.getstr().decode('utf-8'))
        for i in range(num):
            self.stdscr.addstr(f"\nCourse {i+1}:\n")
            course = Course()
            course.input(self.stdscr)
            self.__courses.append(course)

    def input_marks(self):
        self.stdscr.clear()
        if not self.__courses or not self.__students:
            self.stdscr.addstr("Please input students and courses first!\nPress any key...")
            self.stdscr.getch()
            return
        
        self.list_courses(pause=False)
        self.stdscr.addstr("\nSelect a course ID to input marks: ")
        course_id = self.stdscr.getstr().decode('utf-8')
        
        if not any(c.get_id() == course_id for c in self.__courses):
            self.stdscr.addstr("Course not found!\nPress any key...")
            self.stdscr.getch()
            return

        if course_id not in self.__marks:
            self.__marks[course_id] = {}

        self.stdscr.addstr(f"\nEntering marks for course '{course_id}':\n")
        for student in self.__students:
            self.stdscr.addstr(f"  Mark for {student.get_name()} (ID: {student.get_id()}): ")
            raw_mark = float(self.stdscr.getstr().decode('utf-8'))
            
            # Sử dụng math.floor để làm tròn xuống 1 chữ số thập phân
            rounded_mark = math.floor(raw_mark * 10) / 10 
            self.__marks[course_id][student.get_id()] = rounded_mark
            
        self.calculate_gpa() # Tự động tính lại GPA sau khi nhập điểm

    def calculate_gpa(self):
        # Tính GPA bằng numpy array và trọng số (credits)
        for student in self.__students:
            s_marks = []
            s_credits = []
            for course in self.__courses:
                c_id = course.get_id()
                if c_id in self.__marks and student.get_id() in self.__marks[c_id]:
                    s_marks.append(self.__marks[c_id][student.get_id()])
                    s_credits.append(course.get_credits())
            
            if s_credits:
                arr_marks = np.array(s_marks)
                arr_credits = np.array(s_credits)
                gpa = np.average(arr_marks, weights=arr_credits)
                student.set_gpa(gpa)

        # Sắp xếp danh sách sinh viên theo GPA giảm dần
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def list_courses(self, pause=True):
        self.stdscr.clear()
        self.stdscr.addstr("--- List of Courses ---\n")
        for course in self.__courses:
            course.list(self.stdscr)
        if pause:
            self.stdscr.addstr("\nPress any key to continue...")
            self.stdscr.getch()

    def list_students(self):
        self.stdscr.clear()
        self.stdscr.addstr("--- List of Students (Sorted by GPA) ---\n")
        for student in self.__students:
            student.list(self.stdscr)
        self.stdscr.addstr("\nPress any key to continue...")
        self.stdscr.getch()

    def show_student_marks(self):
        self.stdscr.clear()
        if not self.__marks:
            self.stdscr.addstr("No marks have been inputted yet.\nPress any key...")
            self.stdscr.getch()
            return
            
        self.list_courses(pause=False)
        self.stdscr.addstr("\nSelect a course ID to view marks: ")
        course_id = self.stdscr.getstr().decode('utf-8')
        
        if course_id not in self.__marks:
            self.stdscr.addstr("No marks available for this course.\nPress any key...")
            self.stdscr.getch()
            return
            
        self.stdscr.addstr(f"\n--- Marks for Course '{course_id}' ---\n")
        for student in self.__students:
            s_id = student.get_id()
            if s_id in self.__marks[course_id]:
                self.stdscr.addstr(f"  {student.get_name()}: {self.__marks[course_id][s_id]}\n")
        
        self.stdscr.addstr("\nPress any key to continue...")
        self.stdscr.getch()

    def run(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("==============================\n")
            self.stdscr.addstr("  STUDENT MARK MANAGEMENT (PW3)\n")
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
            elif choice == '4': self.list_students()
            elif choice == '5': self.list_courses()
            elif choice == '6': self.show_student_marks()
            elif choice == '0': break

# Curses wrapper để đảm bảo Terminal không bị lỗi nếu code dừng đột ngột
def main(stdscr):
    app = ManagementSystem(stdscr)
    app.run()

if __name__ == "__main__":
    curses.wrapper(main)