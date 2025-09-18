# Store the student GPA and student test score in two variables.
# Using nested conditionals check if the student is eligible for a full scholarship, partial, or no scholarship.
# Scholarship criteria:
# 3.  If a student has a GPA greater or equal to 3.5, and a test score of higher than 65, they’re eligible for a full scholarship.
# a.  If a student has a GPA greater or equal to 3.5, and a test score between 50 and 65, they’re eligible for a partial scholarship.
# b.  If a student has a GPA greater or equal to 3.5 but test score lower than 50, they’re not eligible for a scholarship.
# c.  If a student has a GPA lower than 3.5, they’re not eligible for a scholarship.

# Define student GPA and test score
student_gpa = 4.5
student_score = 75

# Check scholarship eligibility using nested conditionals
if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a partial "
              f"scholarship.")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is eligible for a full scholarship.")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")
else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship.")

