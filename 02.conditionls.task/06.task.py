a = int(input("enter number 1 ="))
b = int(input("enter number 2 ="))
c = int(input("enter number 3 ="))

if a >= b and a >= c:
    print(f" {a} is a larger number")
elif b >= a and b >= c:
    print(f" {b} is a larger number")
else:
    print(f" {c} is a larger number")