# values can not be changed - immutable data_type ( number, string, tuples)


#Number
a = 10 ## integer
b = 10.65 # float
c = 10+6j # complex
print(a,b,c)
print(type(c))

#string(python allow ' or " for string)
a ='welcome to EMG'
b ="Python is great"
print(a,b)
print(type(a))  ## it will print class'str' -- here class because everything is an object, so variable a is object of
# class string.

# tuple -- this consist of a number of values seperated by comma, it is enclosed in parenthesis because you cant
#modify tuple
A = (1,2,3,4,5,'python!')
print(A)
print(type(A))


# values can be changed - mutable data_type ( list, dictionaries, sets )

# List --
X=[1,2,3,4,5,'mukund']
print(X)

# Example of Tuple vs List , so Tuple are faster than list

a = (1,2,3)
b = [1,2,3]

print(dir(a))  # This is tuple
print(dir(b))  # This is list

# so now if you compare of above two o/p you can see which one is faster, because list has more content.

# Dictionaries

# Dictionaries contain key value pairs, Each key is seperated from its value by colo(:), the items are seperated by comma,
# and the whole thing is enclosed within curly braces.

d = {1: 100, 2:200, "hello":[1,2,3]}
print(d)



# Sets is an unordered collection of items, every element is unique and set is created by placing all the items
# (element) inside curly braces {}, seperated by comma.

s = {1,1,2,2,3,3,4,4,5,5}
print(s)

# Now, if you will see the o/p of set it will remove your duplicate entry

