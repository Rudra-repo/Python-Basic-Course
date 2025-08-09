# LET'S PRACTICE :-

# QUE: Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# Using Java.
# I like programming in Java.

f = open("practice.txt","w")
f.write("Hi everyone\nwe are learning File I/O")


f.close()

f = open("practice.txt","a")
f.write("\nusing Java.")

f.close()

f = open("practice.txt","a+")
f.write("\nI like programming in Java.")

f.close()

# QUE: WAP that replace all occurences of "java" with "python" in above file.

f = open("practice.txt","r")
data = f.read()

new_data = data.replace("Java","Python")

print(new_data)

with open("practice.txt","w") as f:
    data = f.write(new_data)


# QUE: Search if the word "learning" exists in the file or not.

f = open("practice.txt","r")
data = f.read()
if(data.find("learning") != -1):
    print("Found")
else:
    print("Not Found")


# QUE: WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.

def chech_for_word():
    f = open("practice.txt","r")
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")

def check_for_line():
    word = "programming"
    data = True
    line_no = 1 
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())


# QUE: Form a file containing numbers separated by comma, print the count of even numbers.

with open("p1.txt","r") as f:
    data = f.read()
    print(data)

num = ""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num += data[i]

count = 0
with open("p1.txt","r") as f:
    data = f.read()

nums = data.split(",")
for val in nums :
    if(int(val)%2 == 0):
        count += 1

    print(count)