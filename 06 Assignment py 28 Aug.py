# 1. LIST CREATION
age_list = [24, 25, 26, 27, 28]
name_list = ["Alice", "Bob", "Charlie", "David", "Eva"]

# 2. LIST OPERATIONS / MODIFICATIONS
# a. Append "Yazhini" to name_list
name_list.append("Yazhini")

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)

# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")

# d. Pop the last element from age_list
age_list.pop()

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])

# f. Sort age_list in descending order
age_list.sort(reverse=True)

# g. Max, Min, and Sum of age_list
print("Max age:", max(age_list))
print("Min age:", min(age_list))
print("Sum of ages:", sum(age_list))

# 3. ACCESSING LIST ELEMENTS
print("First element:", name_list[0])
print("Last element:", name_list[-1])
print("Index 2 to 4:", name_list[2:5])
print("Reversed name_list:", name_list[::-1])

# 4. DICTIONARY OPERATIONS
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 64,
    "Eva": 88
}

# b. Access and print specific student's mark
print("Bob's mark:", student_marks["Bob"])

# c. Add "Janani" with mark 80
student_marks["Janani"] = 80

# d. Update mark of an older student to 82
student_marks["Charlie"] = 82

# e. Print keys, values, and items
print("Keys:", list(student_marks.keys()))
print("Values:", list(student_marks.values()))
print("Items:", list(student_marks.items()))

# 5. SETS OPERATIONS
# a. Set creation and duplicate analysis
# Sets automatically remove duplicates, so repeated values ('a', 'i') are ignored.
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print("my_set output:", my_set)  
# Explanation: Sets store unique elements only, so duplicate entries are ignored.

# b. Modifying by index attempt
try:
    my_set[4] = 's'
except TypeError as e:
    print("Error explanation:", e)
    # Explanation: Sets are unordered and unindexed, so indexing like my_set[4] causes a TypeError.

# c. Create set1 and set2
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Union and Intersection
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# 6. OPERATORS & CONDITIONAL STATEMENTS
try:
    score = float(input("Enter your score (0 to 10): "))
    if 0 <= score <= 10:
        if score > 7:
            print("Above Average: Outstanding performance! Keep up the great work.")
        elif 4 <= score <= 7:
            print("Average: Good effort! Keep practicing, there's room for improvement.")
        else:
            print("Below Average: Need to improve your performance, consistent practice will lead to better results.")
    else:
        print("Please enter a valid score between 0 and 10.")
except ValueError:
    print("Invalid input! Please enter a numerical value.")