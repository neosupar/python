# file - handling

# 1: writing to a file
file_obj = open('hello.txt', 'w')
# write to a file
for i in [1, 2, 3, 4]:
    file_obj.write("Python rocks " + str(i)+'\n')

file_obj.close()

# 2.reading file in single shot

file_obj = open('hello.txt', 'r')

data = file_obj.read()  # reads the full file
print("printing the data it has read:")
print(data)

file_obj.close()

# 3: reading file in chunks read([count])

file_obj = open('hello.txt', 'r')

while 1:
    data = file_obj.read(5)
    if data:
        print(data)
    else:
        break

file_obj.close()

# 4: reading a file line by line

file_obj = open('hello.txt', 'r')

# pythonic way to read line-by-line
for i in file_obj:
    print(i)

file_obj.close()

# 5. reading all the lines and storing that in a list
file_obj = open('hello.txt', 'r')
print(file_obj.readlines())
file_obj.close()

# 6. reading n number of lines where n< total no of line in the file
file_obj = open('hello.txt', 'r')
n = int(input("enter how many lines do you want to read: "))
i = 0
for line in file_obj:
    if i == n:
        break
    i += 1
    print(line)
file_obj.close()

# 7: context-manager: closing the file without .close method
with open('hello.txt', 'r') as file_obj:
    data = file_obj.read()
    print(data)
    print("Inside the block:", file_obj.closed)

print("outside the block:", file_obj.closed)

# # seek(): changes the position of file pointer
# tell() : returns position of file pointer
file_obj = open('hello.txt')
print(file_obj.tell())
file_obj.seek(0, 2)
print(file_obj.tell())
print(file_obj.read())


file_obj.close()








