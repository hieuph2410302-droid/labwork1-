import os
import zipfile
from domains import Student, Course

DAT_FILE = "students.dat"

def save_data(students, courses, marks):
    
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()},{s.get_gpa()}\n")
    
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")
            
    with open("marks.txt", "w", encoding="utf-8") as f:
        for c_id, s_marks in marks.items():
            for s_id, mark in s_marks.items():
                f.write(f"{c_id},{s_id},{mark}\n")

  
    with zipfile.ZipFile(DAT_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write("students.txt")
        zipf.write("courses.txt")
        zipf.write("marks.txt")

   
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")

def load_data():
    students = []
    courses = []
    marks = {}

    
    if os.path.exists(DAT_FILE):
       
        with zipfile.ZipFile(DAT_FILE, 'r') as zipf:
            zipf.extractall()

        
        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        s = Student(parts[0], parts[1], parts[2])
                        s.set_gpa(float(parts[3]))
                        students.append(s)
            os.remove("students.txt")

        
        if os.path.exists("courses.txt"):
            with open("courses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        c = Course(parts[0], parts[1], int(parts[2]))
                        courses.append(c)
            os.remove("courses.txt")

        
        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        c_id, s_id, mark = parts[0], parts[1], float(parts[2])
                        if c_id not in marks:
                            marks[c_id] = {}
                        marks[c_id][s_id] = mark
            os.remove("marks.txt")

    return students, courses, marks