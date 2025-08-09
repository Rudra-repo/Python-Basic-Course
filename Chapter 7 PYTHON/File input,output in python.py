# FILE INPUT/OUTOUT [I/O] IN PYTHON :-
# Python can be used to perform operations on a file. (read & write data) 

# Types of all files
# 1. Text Files : .txt, .docx, .log etc.
# 2. Binary Files : .mp4, .mov, .png, .jpeg etc.

# Open, read & close file :-
# We have to open a file before reading or writing.

# f = open("file_name", "mode")
# "file_name" -> sample.txt, demo.docx
# "mode"  -> r : read mode, w : write mode


f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

# Some types of 'modes' :
# Character             Meaning
# 'r'                   open for reading (default)
# 'w'                   open for writing, truncating the file first (Here, we over writes the info.)
# 'x'                   create a new file and open it for writing
# 'a'                   open for writing, appending to the end of the file if it exists (Here, we are adding info at the end.)
# 'b'                   binary mode
# 't'                   text mode (default)
# '+'                   open a disk file for updating (reading and writing)

f = open("demo.txt", "r")
data = f.read(5)
print(data)

f.close()

# Reading a file

# data = f.read()         # reads entire file
# data = f.readline()     # reads one line at a time.

f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

# Writing to a file :-

# f = open("demo.txt", "w")
# f.write("this is a new line")         # overwrites the entire file

# f = open("demo.txt", "a")
# f.write("this is a new line")         # adds to the file

f = open("demo.txt", "a")
f.write("\nThen I'll move to ReactJS.")

f.close()

f = open("sample.txt", "a+")
# f.write("abc")
print(f.read())
f.write("abc")
f.close()

# 'r+'      read  + overwrite   (pointer is at start)                                          # no truncate(no file data deleted to overwrite)
# 'w+'      read  + overwrite   (pointer position doesn't matter as file data deletes)         # truncate
# 'a+'      read  + append      (pointer is at the end)                                        # no truncate

# 'with' SYNTAX :-

with open("sample.txt", "r") as f:                          # Here, 'as' is used as Alias ( to give another name to sample.txt i.e. "f")
    data = f.read()
    print(data)

# When we are using 'with' syntax , we don't need to worry about closing file as it's already preset to close the file. 

with open("sample.txt", "w") as f:
    f.write("new data")

# DELETING A FILE :-
# using the os module

# Module (like a code library) is a file written by another programmer that generally has a functionns we can use.

# import os
# os.remove(filename)

# import os

# os.remove("sample.txt")


name = "Rudra"
print(f"Hello,{name}\nHow are you?")