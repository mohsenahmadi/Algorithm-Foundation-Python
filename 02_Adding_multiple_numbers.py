#Python Programm to adding multipe numbers based on your count of nums.
import mpmath
count = input("Enter the count of your numbers:")
number = input("Please enter your first number(s):")
sum = int(number)
for i in range(int(count)-1):
		number = input("Enter next: ")
		sum = int(sum) + int(number)
print("The result is: " + str(sum))
