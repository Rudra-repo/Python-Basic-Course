# QUE: WAP to ask the user to enter names of their 3 favourite movies and store them in a list.

movies = []
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
movies.append(input("enter 3rd movie: "))

print(movies)
print(type(movies))


# QUE: WAP to check of a list contains a palindrome of elements. (Hints: use copy() method)
#      [1,2,3,2,1]                  [1,"abc","abc",1]

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not palindrone")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("Palindrone")
else:
    print("not palindrone")

# QUE: WAP to count the number of students with the "A" grade in the following tuple.
#           ["c","d","a","a","b","b","a"]

grade = ("c","d","a","a","b","b","a")
print(grade.count("a"))

# Store the above values in a list & sort them from "a" to "d".

grade = ["c","d","a","a","b","b","a"]
grade.sort()
print(grade)