def draw_stars(myList):
	for item in myList:
		if (type(item) == int):
			print('*' * item)
		elif (type(item) == str):
				print(item[0].lower() * len(item))

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)