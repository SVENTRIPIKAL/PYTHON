"""
	Program creates an empty Dictionary
	and updates it with a score eval
	according to each student's grades.
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
} ;


student_grades = {} ;


for key in student_scores:
    if (student_scores[key] <= 70):
        grade = "Fail" ;
    elif (student_scores[key] <= 80):
        grade = "Acceptable" ;
    elif (student_scores[key] <= 90):
        grade = "Exceeds Expectations" ;
    else:
        grade = "Outstanding" ;
    student_grades[key] = grade ;


print(student_grades) ;
