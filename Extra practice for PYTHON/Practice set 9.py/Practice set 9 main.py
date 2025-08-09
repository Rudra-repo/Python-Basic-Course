# QUE: WAP to read the text from a given file "poems.txt" and find out whether it contains the word 'twinkle'.

f = open("poems.txt")
C = f.read()
if("twinkle" in C):
    print("Yes, it contains the word 'twinkle' .")
else:
    print("NO, the word 'twinkle' isnot present in it. ")
f.close()

# QUE: 
