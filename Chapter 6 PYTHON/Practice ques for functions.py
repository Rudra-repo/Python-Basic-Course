# QUE: WAF to print the length of a list. (list is the parameter)

heroes = ["thor", "ironman", "captain america", "shaktiman"]
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]

print(heroes[0], end =" ")
print(heroes[1])
def print_len(list):
    print(len(list))

print_len(heroes)
print_len(cities)


# QUE: WAF to print the elements of a list in a single line. (list is the parameter)

def print_list(list):
    for items in list:
        print(items, end=" ")

print_list(heroes)
print()

print_list(cities)
print()


# QUE: WAF to find the factorial n. (n is the parameter)

n = 5 
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)


cal_fact(6)


# QUE: WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")

converter(1000)


# QUE: WAP to show wheather a number is even or odd using functions.

def num(num):
    if(num%2 == 0):
        print("EVEN")
    else:
        print("ODD")

num(37)
