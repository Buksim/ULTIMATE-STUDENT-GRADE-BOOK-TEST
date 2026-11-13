# Student Grade Book TEST.py

students_marks = {
    "Sammy": 99,
    "Edunjobi": 70,
    "Raymond": 65,
    "Oyekan": 89,
    "Tolubori": 75
}

# Calculate the average mark
total_marks = 0
for mark in students_marks.values():
    total = total + mark
    average = total / len(students_marks)
    
    print("Class Average: ", average)
    
# Find the Highest and Bottom Scorers in the Test 
highest_scorer = max(students_marks, key=students_marks.get)
lowest_scorer = min(students_marks, key=students_marks.get)

print(f"Top Student & Overall Best Scorer: {highest_scorer} with a score of {students_marks[highest_scorer]}")
print(f"Lowest Student: {lowest_scorer} with a score of {students_marks[lowest_scorer]}")

# How to search for a Student's Score in the Test
name = input("Enter a Student Name: ")
score = students_marks.get(name)

if score is not None:
    print(name, "scored", score)
else:
    print("Student not found in the grade book.")