cheracter = input("enter cheracter = ")
vowels = "aeiou"
if cheracter.lower() in vowels:
    print(f"{cheracter} is a vowels.")
else:
    print(f"{cheracter} is a consonant.")