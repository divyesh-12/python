a = int(input("enter first number : "))
b = int(input("enter secound number : "))
operater = input("enter operater(+,-,*,/) : ")

match operater:
    case "+": print(a + b)
    case "-": print(a - b)
    case "*": print(a * b)
    case "/":
        if b == 0:
            print("not devide by zero")
        else:
            print(a / b)
    case _: print("Invalid Number")