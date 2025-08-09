str = "I am a coder."

# str.endswith("er.")             # returns true if string ends with substr
# str.capitalize()                # capitalizes 1st character
# str.replace( old, new )         # replaces all occurrences of old with new
# str.find(word)                  # returns 1st index of 1st occurrence
# str.count("am")                 # counts the occurrence of substr in string


# str.endwith("xyz")
str = "I am studying python from Youtube"
print(str.endswith("ube"))
print(str.endswith("be."))

# str.capitalize()
str = "i am studying python from youtube"
print(str.capitalize())                 # This function does not captilize letter in original string (original string remains same as the previous one.)
print(str)
# if we want changes in our original string 
str = str.capitalize()
print(str)

# str.replace( old, new )
str = "i am studying python from youtube"
print(str.replace("python", "javascript"))

# str.find("word")
str = "i am studying python from youtube"               # It gives starting index of word,letter (first letter index only.)
print(str.find("o"))

#str.count("word")
str = "i am a student and student should study with full focus"
print(str.count("student"))

# Escape Sequence Character :-

# Sequence of characters after backslash "\"-Escape Sequence characters
# Escape Sequence characters comprise of more than one character but represent one character when used within the strings.

# Examples:
# \n            # For new line
# \t            # For tab space
# \'            # For single quote
# \\            # For backslash
