#Python Programm to solving first degree equation. the users must be set the A and B and C as three important factors of this equations.
import mpmath
print("Please enter factors of this equation. We can solve a(x)+b=c")
a = float(input("Enter A:"))
b = float(input("Enter B:"))
c = float(input("Enter C:"))
x = (c - b) / a
print("The result (x) is: " + str(x))
