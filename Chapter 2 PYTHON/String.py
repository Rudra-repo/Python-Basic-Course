## STRINGS 
# String is data type that stores a sequence of characters.

# Basic operations                                  # Escape Sequence characters. -----> these are special characters which is used for formatting like tab [\t], next line [\n]

# Concatenation
print("Hello" + " World")

# Lenght of str
# len(str)

str1 = "This is a string."
str2 = 'Rudra'
str3 = """this is a book."""

"this is python's tutorial"             # Here, single quote is used in statement , so to avoid this situation we generally use double quotes.

str1 = "This is a string.We are creating it in python."
print(str1)


# Concatenation 

str1 = "Hello"
str2 = " World"

print(str1+str2)

str1 = "Rudra"
str2 = "Pratap"
final_str = str1 + " " + str2
print(len(final_str))
print(final_str)
print(len(str1))
print(len(str2))


## Indexing :-
# Indexing start from zero to so on. While numbering, we have to take care that space or underscores , numbering has to be assigned.
 
str = "Rudra Pratap"
ch = str[6]
print(ch)                   # We can only access the string index but can't change the string index[No letter can be replaced, it only shows the indexing of string]

