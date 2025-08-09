# RECURSION :-
# When a function calls itself repeatedly.          # Recursion is similar to Loop but in some cases, we use recursion, as it make it simple and easy to code.
#                                                  # Most of the cases, we use loop but in some cases of data structure to code it simply.
# prints n to 1 backwards

# Recursive function:
def show(n):
    if(n == 0):        # this is Base Case, which decides that where the loop has to stop
        return
    print(n)
    show(n-1)

show(5)      # 5,4,3,2,1

# Call Stack : As the function performs and completes it's cycle this forms a layer and recheck the condition and then again run that cycle in a loop. So, these layers are called call stack(as name suggest it's meaning.)

# returns n!

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))

# LET'S PRACTICE :-

# QUE: Write a recursive function to calculate the sum of first n natural numbers.

def show(n):
    if(n == 0):
        return 0
    return show(n-1) + n

sum = show(5)
print(sum)

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "litcho", "apple", "banana"]

print_list(fruits)