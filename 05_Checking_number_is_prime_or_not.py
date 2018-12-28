#Python Programm to checking your number is prime or not.
import mpmath
num = int(input("Enter your number:"))
for i in range(2, num):
	if (num % i) == 0:
		print(num, "is not prime number")
		break
else:
	print(num, "is prime number")
