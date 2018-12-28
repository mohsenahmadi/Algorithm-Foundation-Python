#Python Programm to split digits of your numbers. Your number must be 3 digit.
import mpmath
num = int(input("Enter your number:"))
if num < 1000 and	num > 99:
	d1 = int(num % 10)
	d2 = int(((num / 10) % 10))
	d3 = int(((num // 100)))
	print ("First Digit is: " + str(d3),  "\nSecend Digit is: " + str(d2), "\nAnd Third Digit is: " + str(d1))
else:
	print("NUMBER is OUT of RANGE")
	
	
	
