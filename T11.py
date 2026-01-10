#Create a dictionary of 5 students with their marks and find the total marks

# Create a dictionary with student names as keys and marks as values
student_marks = {
    "Archit": 85,
    "Utsav": 78,
    "Jash": 92,
    "Dev": 88,
    "Ram": 95
}

# Calculate total marks using sum() on dictionary values
total_marks = sum(student_marks.values())

print("Student Marks:", student_marks)
print("Total Marks:", total_marks)
