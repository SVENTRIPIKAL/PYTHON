"""
	Program receives and converts
	user input scores into a list,
	and prints the highest score
	from the list without the use
	of the max() function.
"""

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)


max = student_scores[0] ;

for score in student_scores:
    if (score > max):
        max = score ;

print(f"The highest score in the class is: {max}") ;

