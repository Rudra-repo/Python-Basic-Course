# These are the QUE by 'Code with Harry' for practice :-

# QUE: WAP to print 'Twinkle Twinkle Little Star' poem in python.

print("""
      Twinkle, twinkle, little star,
      how I wonder what you are.
      Up above the world so high,
      like a diamond in the sky.
      
      Twinkle, twinkle, little star,
      how I wonder what you are.
      When the blazing sun is set,
      and the grass with dew is wet.
      Then you show your little light,
      twinkle, twinkle all the night.
      Twinkle, twinkle little star,
      how I wonder what you are.

      Then the traveler in the dark thanks you for your tiny spark.
      How could he see where to go if you did not twinkle so?
      Twinkle, twinkle little star, how I wonder what you are.
      
      As your bright and tiny spark lights the traveler in the dark,
      though I know not what you are, twinkle, twinkle, little star.
      Twinkle, twinkle, little star, how I wonder what you are.\n"""
)

# QUE: Use REPL and print the table of 5 using it.

print("Table of 5 using REPL.")
print("5*1=", 5*1)
print("5*2=", 5*2)
print("5*3=", 5*3)
print("5*4=", 5*4)
print("5*5=", 5*5)
print("5*6=", 5*6)
print("5*7=", 5*7)
print("5*8=", 5*8)
print("5*9=", 5*9)
print("5*10=", 5*10)

# QUE: Install an external module and use it to perform an operation of your intrest.

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Hello, Rudra. How are you?")
engine.runAndWait()

# QUE: WAP to print the contents of a directory using the os module

import os

# Ask the user to input a directory path
directory = input("Enter the path of the directory: ")

# Check if the directory exists
if os.path.exists(directory):
    print(f"\nContents of directory '{directory}':\n")
    
    # List all files and directories
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified directory does not exist.")

# QUE: Label the program written in problem 4 with comments.

import os

# Input directory path
directory = input("Enter the path of the directory: ")

# Directory exists or not
if os.path.exists(directory):
    print(f"\nContents of directory '{directory}':\n")
    # Items in directory
    for item in os.listdir(directory):
        print(item)
else:
    print("The specified directory does not exist.")
