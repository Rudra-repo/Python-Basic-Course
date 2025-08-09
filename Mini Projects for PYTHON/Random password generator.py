import random
import string

password_len = 8
charValues = string.punctuation + string.ascii_letters + string.digits

# list comprehension [function for i in range(n)]
password = "".join([random.choice(charValues) for i in range(password_len)])


# password = ""
# for i in range(password_len):
#     password += random.choice(charValues)

# print(password)

print("your random password is:", password)