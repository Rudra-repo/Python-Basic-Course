# Punctuators aare symbols to organize structure in programming.
    # (),{},@,[],# etc.
# -=,+=,/=,*=,//=,= etc are also punctuators.


#  Expression Execution :-

A,B=2,3
Txt="@"                 # String and numeric value can operate together with * .
print(2*Txt*3)


A,B="2",3
Txt="@"                 # String and string can operate together with + .
print((A+Txt)*B)

A,B=12,5
C=A//B                 # '//' , this symbol represent the same as GIF( Greatest Integer function) , as above line mentioned then only it gives float value otherwise it gives int value. 
print(C)


# Remainder is negative when denominator is negative 

A,B=-5,2 # ("%" is a modulo sign)
C=A%B                       # The denominator is positive, so remainder is positive 
print(C)


A,B=5,-2
C=A%B                       # The denominator is negative, so remainder is negative. 
print(C)

A,B=-5,-2
C=A%B                       # The denominator is negative, so the remainder is also negative.
print(C)

A,B=2,3
C=4                      # Numeric values can operates with all the arithmetic operators.
print(A+B*C)

A,B=10,5.0
C=A*B                    # Arithmetic expression with integers and float will result in float.
print(C)


A,B=1,2
C=A/B                   # Result of division operators with two integers will be float.
print(C)


A,B=1.5,3
C=A//B                  # Integer division with float and int give int displayed as float.
print(C,A/B)            



