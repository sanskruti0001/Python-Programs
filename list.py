grocery_list = ["Milk", "orange", 1,2,3,True, 2+4j, 2.3]
print(grocery_list)

print(grocery_list[0])
print(grocery_list[-1])
print(grocery_list[1:])
print(grocery_list[1:4])
print(grocery_list[1:5])
      
movies = ["Action1" , "Action2" , "Action3" , "Comedy1"]
print(movies[0:3])

pages = ["Title page" , "chap1" , "chap2" , "conclusion" , "index"]
print(pages[-1])

print(pages[-2])

queue = ["Ajay" , "Bijay" , "Sanjay" , "Anjay"]
print(queue[-1])
print(queue[-2])

list1 = ["Apple" , "banana"]
print(list1)

list1.append("orange")
print(list1)

playlist = []
playlist.append("Saare jaha se acha")
playlist.append("Ae mere vatan ke logo")

print(playlist)

bookshelf = []
bookshelf.append("book1")
bookshelf.append("book2")

print(bookshelf)

list1[1] = "brinjal"
print(list1[1])

list1.insert(1, "banana")
print(list1)

bus_seat = ["Ajay", "Bob", "Sanjay"]
bus_seat.insert(1,"Ram")

print(bus_seat)


my_list = ["Apple", "Banana", "Orange"]
brothers_list= ["brinjal", "potato"]

print(my_list)
print(brothers_list)
print(my_list + brothers_list)










#repetation operation

print("*" * 5)
print("-" * 5)
print([0] * 5)
print([1,2,3] * 10)
print(list(range(1,6))*3)


msg="your appointment is tomorrow\n"
print(msg * 5)


print(grocery_list)
"milk" in grocery_list
"Banana" in grocery_list
"Banana" not in grocery_list
print(grocery_list)