# 1. String Concatenation
string1 = "Hello "
name = input("Enter your Name: ")
concatenated_str = string1 + name
print(concatenated_str)

string3 = ", welcome to Python programming"
final_str = concatenated_str + string3
print(final_str)

print("-" * 40)

# 2. String Slicing and Indexing
# Using final_str from part 1: "Hello Zara, welcome to Python programming"
a = final_str[0]
b = final_str[-1]
c = final_str[:5]
d = final_str[-11:]
e = final_str[::-1]

# To slice "Python" dynamically or directly:
start_idx = final_str.find("Python")
f = final_str[start_idx : start_idx + 6]

print("a. First character:", a)
print("b. Last character:", b)
print("c. First 5 characters:", c)
print("d. Last 11 characters:", d)
print("e. Reversed string:", e)
print("f. Sliced word:", f)

print("-" * 40)

# 3. String Methods

strM = "Python beginner tutorial"

print("a. Uppercase:", strM.upper())
print("b. Lowercase:", strM.lower())
print("c. Capitalize:", strM.capitalize())
print("d. Count of 't':", strM.count("t"))
print("e. Replaced string:", strM.replace("Python", "Machine Learning"))

print("-" * 40)

# Tuples (Creation, Modification and Access)

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate tuples
t_combine = tuple1 + tuple2
print("a. t_combine:", t_combine)

# b. Repeat elements 3 times
t_repeated = t_combine * 3
print("b. Repeated tuple:", t_repeated)

# c. Access 3rd element (index 2)
print("c. 3rd element:", t_combine[2])

# d. Access first three elements
print("d. First three elements:", t_combine[:3])

# e. Access last three elements
print("e. Last three elements:", t_combine[-3:])