members = ["jack", "bob", "john"]
def check(costumer): return "Discount" if costumer in members else "No discount"
print(check("bob"))

# Store the student GPA and student test score in two variables.
# Using nested conditionals check if the student is eligible for a full scholarship, partial, or no scholarship.
# Scholarship criteria:
# 3.  If a student has a GPA greater or equal to 3.5, and a test score of higher than 65, they’re eligible for a full scholarship.
# a.  If a student has a GPA greater or equal to 3.5, and a test score between 50 and 65, they’re eligible for a partial scholarship.
# b.  If a student has a GPA greater or equal to 3.5 but test score lower than 50, they’re not eligible for a scholarship.
# c.  If a student has a GPA lower than 3.5, they’re not eligible for a scholarship.

student_gpa = 4.2
student_test_score = 76

if student_gpa <= 3.5 and student_test_score < 65:
    print("You are eligible for a Full Scholarship")
elif student_gpa <= 3.5 and 50 <= student_test_score <= 65:
    print("You are eligible for a Partial Scholarship")
elif student_gpa <= 3.5 and 50 < student_test_score:
    print("You are not eligible for a Scholarship")
else: student_gpa => 3.5:
print("You are not eligible for a Scholarship")


