# QUE: Print numbers from 1 to 100.

count = 1
while count <= 100 :
        print(count)
        count += 1 

# QUE: Print number from 100 to 1.
 
count = 100
while count >= 1 :
        print(count)
        count -= 1

# QUE: Print the multiplication table of a number n.

n = 1
while n <= 10 :
        print(3*n)
        n += 1


#  QUE: Print the elements of the following list using the loop: [1,4,9,16,25,36,49,64,81,100]

i = 1 
while i <= 10 :
        print(i*i)                   # This is basically for square upto 10 with loop.
        i += 1

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx <= 9:                       # this is correct with respect to the "QUE".
        print(nums[idx])
        idx += 1

heroes = ["ironman", "thor", "superman", "batman"]

# Traverse ( like this way, if travel index by index on every element in tuple or list , we call it traverse)
idx = 0 
while idx < len(heroes):
        print(heroes[idx])
        idx += 1

# QUE: Search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36
idx = 0
while idx < len(nums):
        if(nums[idx] == x):
                print("Found at idx", idx)
        idx += 1

