## SLICING :-
# Accessing parts of a string :-

       # str[ starting_idx : ending idx ]                  # ending idx is not included 

str = "Rudra_Pratap"
C = str[ 1 : 4 ]  # is "udr".             # like the letter at index '4' is not included in this ques.
print(C)

D = str[  : 5]      # is equal to D = str[ 0 : 5 ]   
print(D) 

# Similarly, str[ 1 :  ] is same as str[ 1 : len(str) ]

E = str[ 6 :  ]
print(E)

# Negative Index
                     # Negative index start from last of the string and rest same rules followed . 
str = "Apple"        # like A  P  P  L  E
A = str[-3:-1]       #     -5 -4 -3 -2 -1.      # THE letter on index '-1' is not included in this ques. 
print(A) 

# Slicing with skip value:-
# WE can provide a skip value as a part of our slice like this :
word = "amazing"
A = word[1:6:2]
print(A)

a = "0123456789"
b = a[1:7:3]
print(b)
