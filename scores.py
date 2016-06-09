print "Scores and Grades"
a = 0
while a < 10:
	score = input()
	if score <101 and score > 89:
		print "Score: ", score, "; Your grade is A"
	elif score < 90 and score > 79:
		print "Score: ", score, "; Your grade is B"
	elif score < 80 and score > 69:
		print "Score: ", score, "; Your grade is C"
	elif score < 70 and score > 59:
		print "Score: ", score, "; Your grade is D"
	a += 1
print "End of the program. Bye!"