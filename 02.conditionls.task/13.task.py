a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if (a == b == c):
    print("Type : Equilateral")
elif (a == b or b == c or a == c):
    print("Type : Isosceles")
else:
    print("Type : Scalene")