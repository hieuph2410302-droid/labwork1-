# Initialize global variables to store data
students = []
courses = []
marks = {}

# --- INPUT FUNCTIONS ---

def input_students():
    """Input the number of students and their information"""
    num_students = int(input("Enter number of students in the class: ")) #[cite: 8]
    for i in range(num_students):
        print(f"\nStudent {i+1}:")
        s_id = input("  ID: ")
        name = input("  Name: ")
        dob = input("  Date of Birth (DD/MM/YYYY): ")
        # Append student information to the list
        students.append({"id": s_id, "name": name, "dob": dob}) #[cite: 8]

def input_courses():
    """Input the number of courses and their information"""
    num_courses = int(input("\nEnter number of courses: ")) #[cite: 8]
    for i in range(num_courses):
        print(f"\nCourse {i+1}:")
        c_id = input("  ID: ")
        name = input("  Name: ")
        # Append course information to the list
        courses.append({"id": c_id, "name": name}) #[cite: 8]

def input_marks():
    """Select a course and input marks for students in this course"""
    if not courses or not students:
        print("\nPlease input students and courses first!")
        return
    
    list_courses()
    course_id = input("\nSelect a course ID to input marks: ") #[cite: 8]
    
    # Check if the course exists
    if not any(c['id'] == course_id for c in courses):
        print("Course not found!")
        return

    # Initialize the dictionary to store marks for this course if it doesn't exist
    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEntering marks for course '{course_id}':")
    for student in students:
        mark = float(input(f"  Mark for {student['name']} (ID: {student['id']}): ")) #[cite: 8]
        marks[course_id][student['id']] = mark

# --- LISTING FUNCTIONS ---

def list_courses():
    """List all courses"""
    print("\n--- List of Courses ---") #[cite: 8]
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")

def list_students():
    """List all students"""
    print("\n--- List of Students ---") #[cite: 8]
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")

def show_student_marks():
    """Show student marks for a given course"""
    if not marks:
        print("\nNo marks have been inputted yet.")
        return
        
    list_courses()
    course_id = input("\nSelect a course ID to view marks: ") #[cite: 8]
    
    if course_id not in marks:
        print("No marks available for this course.")
        return
        
    print(f"\n--- Marks for Course '{course_id}' ---") #[cite: 8]
    for student in students:
        s_id = student['id']
        if s_id in marks[course_id]:
            print(f"  {student['name']} (ID: {s_id}): {marks[course_id][s_id]}")

# --- MAIN PROGRAM ---

def main():
    while True:
        print("\n" + "="*30)
        print("  STUDENT MARK MANAGEMENT")
        print("="*30)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-6): ")
        
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()