import random
print "Coin Toss!"
a = 0
b = 0
c = 0
while a < 5001:
	random_num = random.randint(0,1)
	if random_num == 0:
		b += 1
		print "Throwing a coin... it's heads! Got", b, "heads so far and", c, "tails so far!"
	elif random_num == 1:
		c += 1
		print "Throwing a coin... it's tails! Got", b, "heads so far and", c, "tails so far!"
	a += 1