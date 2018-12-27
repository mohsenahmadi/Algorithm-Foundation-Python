#Python Programm to check your enter number is odd or even

import mpmath
print("This program checking your enter number is odd or even")
number = input("Please enter your number:")
number = int(number)
if mpmath.fmod(number,2):
	print("Your number is {0} and it's odd".format(number))
else:
	print("Your number is {0} and it's even".format(number))
