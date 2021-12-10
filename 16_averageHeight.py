"""
	Program converts user input
	to a list of heights and
	calculates the average of
	the heights, rounded to the
	nearest whole, without the use
	of sum() and len() functions.
"""

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


sum = 0 ;       count = 0 ;

for height in student_heights:
    sum += height ;
    count += 1 ;

average = round( sum / count ) ;

print( average ) ;

