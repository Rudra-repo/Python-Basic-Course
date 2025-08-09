# input() statements is used to accept values (using keyboard) from user :-

# string input 
#  name = input("name : ")

# int input 
# age = int(input("age : "))

# float input
#  price = float(input("price : "))


# Taking input from user & printing it 

name = input("name : ")
age = int(input("age : "))
price = float(input("price : "))

print("My name is", name, "and I am", age, "years old")
print("Price of the product is", price) 


name = input("enter your name: ")
print("Welcome", name)

# If we take direct input then there's only single datatype i.e. String , int values also coverted to string like "45" similar with floating value "99.89"
# To solve this problem we have to use 'TYPE CASTING' , we get desired result after type casting.

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("Welcome", name)
print("age =", age)
print("marks =", marks)