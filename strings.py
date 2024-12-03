char = "A"
print(ord(char))
print(ord("B"))
print(ord("a"))
print(chr(101))

string1 = "hello"
string2 = "world"

print(string1 +", " +string2)
print("String" + ">" +"concatenation")

# Modification of String

s = "I am Sanskruti"
print(s.replace('Sanskruti' ,'sakshi'))

txt = ("BRB , TTYL , LOL")
print(txt.replace('BRB' , 'Be right back').replace('TTYL' , 'Talk to you Later').replace('LOL', 'Laugh out Loud'))

text = 'Sanskruti'
print(text.lower())
print(text.upper())
print(text.title())

text1 = "I am Is A Student"
print(text1.swapcase())

print(text1.capitalize())

text2 = ' I am a student at ITP'
print("f" in text2)

sentence = "I am a student at ITP"
search_word = "am"

if search_word in sentence:
    print("The search word is present")
else:
    print("Not")


email = "sk66@gmail.com"
if "@" in email :
   print("valid email") 
else :
    print("Invalid")


document = "some_file.pdf"
if ".pdf" in document:
    print("its a pdf file")
else:
    print("Not")

# String Comparision

str1 = "Hello"
str2 = "hello"

print(str1 == str2)    

str1 = "SANSKRUTI"
str2 = "SANSKRUTI"

print(str1 == str2)   

str1 = "Hello"
str2 = "hello"

print(str1.lower() == str2.upper())    

reg_username = ["Sanskruti" , "Sanskruti" , "Sanskruti"]
new_user = "Sanskruti21"

if new_user in reg_username:
    print("already in use")
else:
    print("username is available")


product_code  = "P123"
scanned_code = input("scan the product code : ")

if product_code == scanned_code:
    print("The price is 100")
else:
    print("talk to reception")

names = ["Sanskruti", "Mukund", "Kolekar"]
print(sorted(names))    

playlist = ["KKHH", "Magic", "Hello", "Magic"]
print(sorted(playlist))


# String Operations

input_str = "       sanskruti       "
print(input_str.strip())


input_str = "       Hello World        "
print(input_str.strip())

csv_row = "Apple     " 
print(csv_row.strip())

data = "Ajay, data science, teacher"
print(data)

teacher_info  = data.split('.')
print(teacher_info)

print(name = teacher_info[0])
print(sub = teacher_info[1])
print(des = teacher_info[2])