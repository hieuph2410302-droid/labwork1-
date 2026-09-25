# File: input_data.py

# Khởi tạo các biến toàn cục để lưu trữ dữ liệu
students = []
courses = []
marks = {}

def input_students():
    """Input the number of students and their information"""
    num_students = int(input("Enter number of students in the class: "))
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        s_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  Date of Birth (DD/MM/YYYY): ")
        students.append({"id": s_id, "name": name, "dob": dob})

def input_courses():
    """Input the number of courses and their information"""
    num_courses = int(input("\nEnter number of courses: "))
    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        c_id = input("  ID: ")
        name = input("  Name: ")
        courses.append({"id": c_id, "name": name})

def input_marks():
    """Select a course and input marks for students"""
    if not courses or not students:
        print("\nPlease input students and courses first!")
        return
    
    # Hiển thị danh sách khóa học ngay tại đây để tránh lỗi import vòng
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")
        
    course_id = input("\nSelect a course ID to input marks: ")
    
    if not any(c['id'] == course_id for c in courses):
        print("Course not found!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEntering marks for course '{course_id}':")
    for student in students:
        mark = float(input(f"  Mark for {student['name']} (ID: {student['id']}): "))
        marks[course_id][student['id']] = mark