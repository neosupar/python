################################################# Arthmetic Operation ##################################################
a = 10
b = 20
###############
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# modulus
print(a%b)
# Exponent
print(a**b)
# Floor Division
print(a//b)

################################################ Assignment Operation ##################################################
a = 30
b = 45
############
print(a+b)  # a += b
print(a-b)  # a -= b
print(a*b)  # a *= b
print(a/b)  # a /= b
print(a**b) # a**= b
print(a//b) # a//= b

################################################ Comparison Operation ##################################################
a = 30
b = 45
########
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

################################################ Logical Operation ##################################################
a = 78
b = 45
########
print(a and b) # it will return a, if a is false, b otherwise -
# which means if both value will be true then only it will give you true, it is like multiplication
# tru*true = true, if either of the value is false the o/p will be false. so 1*0 = 0 and 0*1 = 0
print(a or b)  ## return b, if b is False, a otherwise - this means if either of the value is true the o/p will be
# true. so or is like addition. for example - 0+100 = 100
print( not a)  ## Return true , it a is true, false otherwise, this is basically opposite.

# if i want to get the binary data of any value so use like this - a = 12 then type bin(12) so it will give o/p of
# 12 binary number

################################################ Bitwise Operation ##################################################
a = 78
b = 45
########
print(a&b) # Binary AND
print(a|b) # Binary OR
print(a^b) # Binary XOR
# print(a~b) Binary NOT ( not working not sure why )
# print(a<<) Binary left shift ( not working not sure why )
print(a>>b) # Binary right shift

################################################ Identity Operation ##################################################
a = 20
b = b
######## it checks if the both object store the same value or not in memory

if(a is b):
    print(" Line 1 >> a and b have same identity ")
else:
    print(" Line 1 >> a and b do not have same identity ")

b = 40
if(id(a) == id(b)):
    print("Line 2 >> a and b have same identity ")
else:
    print("Line 2 >> a and b do not have same identity ")

if(a is not b):
    print(" Line 3 >> a and b have same identity ")
else:
    print(" Line 3 >> a and b do not have same identity ")

################################################ Membership Operation ##################################################
a = 23
b = 20
list = [1, 2, 3, 23, 20]
######## so basically it check whether particular thing which we are checking is present in the list or not

if ( a in list ):
   print ("Line 1 - a is available in the given list")
else:
   print ("Line 1 - a is not available in the given list")

if ( b not in list ):
   print ("Line 2 - b is not available in the given list")
else:
   print ("Line 2 - b is available in the given list")

a = 2
if ( a in list ):
   print ("Line 3 - a is available in the given list")
else:
   print ("Line 3 - a is not available in the given list")







