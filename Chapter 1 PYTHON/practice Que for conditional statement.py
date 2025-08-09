# QUE:
# PRINT OUTPUT FOR :
# A = 5 & G = M
# A = 2 & G = F

A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("No fee")

    #   BEST PRACTICES
    # Calculate simple intrest 
   
    p = float(input("p : "))
    t = float(input("t : "))
    r = float(input("r : "))
    SI = (p*r*t)/100
    print(SI)