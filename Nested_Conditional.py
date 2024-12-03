# Greatest among three numbers

num1 = int (input("Enter first number :"))
num2 = int (input("Enter second number :"))
num3 = int (input("Enter third number :"))

if num1 >= num2 and num1 >= num3:
   largest = num1
elif num2 >= num1 and num2 >= num3:
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

# Check Temperature 

temperature = int (input("Enter temperature :"))

if temperature < 15:
    print(" Cold ")
else:
    if temperature <= 30:
        print(" Warm ")
    else:
        print(" Hot ")


# Driving Eligibility


age = int(input("Enter your age: "))
valid_license = input("Do you have a valid driving license? (yes/no): ")


if age >= 18:
    if valid_license == 'yes':
        print("You are eligible to drive!")
    else:
        print("You must have a valid driving license to drive.")
else:
    print("You must be 18 or older to drive.")


# Vowel and consonant

char = input("Enter a character: ")

if char.isalpha() and len(char) == 1:
    
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Please enter a valid single alphabet character.")