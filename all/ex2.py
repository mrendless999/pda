# List of tuples with student names and their marks
students = [ 
    ("Alice", 85), 
    ("Bob", 67), 
    ("Charlie", 92), 
    ("David", 76), 
    ("Alice", 85),  # Duplicate entry 
    ("Eva", 88) 
] 

# 1. Dictionary Creation (Student names as keys, marks as values)
# If a name occurs more than once, the last occurrence is stored in the dictionary
student_dict = {name: marks for name, marks in students}

# 2. Find the student with the highest marks
highest_student = max(student_dict, key=student_dict.get)
print(f"Student with the highest marks: {highest_student}, Marks: {student_dict[highest_student]}")

# 3. Display all students with marks above 75
students_above_75 = [name for name, marks in student_dict.items() if marks > 75]
print(f"Students with marks above 75: {students_above_75}")

# 4. Remove duplicate names (if any) using a set
unique_students = set([name for name, marks in students])
print(f"Unique student names: {unique_students}")

# 5. Concatenate all student names into a single string separated by commas
student_names = ', '.join(unique_students)
print(f"Concatenated student names: {student_names}")

# 6. Sort the students by their marks in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Students sorted by marks (descending):")
for name, marks in sorted_students:
    print(f"{name}: {marks}")
