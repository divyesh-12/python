age = int(input("Enter Age : "))
day_type = input("Enter weekday/weekend : ")

if age < 12:
    price = 100
elif age <= 59:
    price = 200
else :
    price = 150
    
if day_type == "weekend":
    price = price + 20
print(price)