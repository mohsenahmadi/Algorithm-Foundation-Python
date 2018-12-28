#Python Programm to calculate prime diviser of your entered number
import mpmath
num = int(input("Enter your number:"))
for i in range(1, num+1):
	if num % i == 0:
		print("{0} prime diviser to:".format(num), i )

