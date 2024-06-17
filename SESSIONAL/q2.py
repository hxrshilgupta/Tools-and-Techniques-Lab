def create_student_dict():
  
  students = {}
  num_students = int(input("Enter the number of students: "))
  for i in range(num_students):
    roll_number = int(input("Enter roll number for student {}: ".format(i+1)))
    student_name = input("Enter student name: ")
    students[roll_number] = student_name
  return students

def display_students(students):
 
  print("\nStudent List:")
  for roll, name in students.items():
    print(f"Roll Number: {roll}, Name: {name}")

def add_student(students):
 
  print("\nAdding a new student...")
  new_roll = int(input("Enter roll number for new student: "))
  new_name = input("Enter student name: ")
  students[new_roll] = new_name
  return students

def main():
  
  students = create_student_dict()
  display_students(students)

  # Option to add a new student
  choice = input("\nDo you want to add a new student? (y/n): ")
  if choice.lower() == 'y':
    students = add_student(students)
    display_students(students)

  print("\nStudent data management complete.")

if __name__ == "__main__":
  main()
