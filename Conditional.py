# +ve or -ve

num = int (input("Enter a number :"))

if(num>0):
     print("Positive number")
elif (num ==0 ):
     print("Zero")
else :
   print("Negative number")    



# Even or Odd

num = int (input("Enter a number :"))

if(num%2==0):
     print("Even number")

else :
     print("Negative number")  


# Grade Checker


grade = int (input("Enter Marks :"))

if( grade > 90  and grade <100 ):
     print("Grade A")

elif grade > 70 and grade < 89 :
     print("Grade B ")

elif grade > 50 and grade < 69 :
     print("Grade C ")

elif grade > 50 and grade < 69 :
     print("Grade C ") 

elif grade < 50 :
     print("Grade F ")     

# Check Divisibility

num = int (input("Enter Marks :"))

if num % 5 == 0 and num % 3 == 0:
     print ("Divisible by both 5 and 3")
elif  num % 5 == 0 :
     print ("Divisible by  5")
elif  num % 3 == 0 :   
      print ("Divisible by  3")


# Minimum from two numbers

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

if a < b:
    print("Smallest one is: ",a)
elif a > b:
    print("Smallest one is: ",b)
else:
    print("Both are equal")
       




