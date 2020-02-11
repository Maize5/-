#!/usr/bin/env python3
x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
	term *= x / n
<<<<<<< HEAD
	result += term
	n += 1
	print("n = {}, term = {}, result = {}".format(n, term, result))
	if term < 0.0001:
		break
print("No of Times= {} and Sum= {}".format(n, result))
=======
	result
>>>>>>> 30981946a2344e99a3d0dd3a75f67aadfeabde30
