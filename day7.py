
# numbers = [10, 20, 30]

# numbers.append(40)
# print(numbers)

# numbers.insert(1, 15)
# print(numbers)

# numbers.remove(30)
# print(numbers)

# numbers.pop()
# print(numbers)




# numbers = [10, 20, 30, 40]
# for num in numbers:
#     print(num)




numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[::-1]) # [50, 40, 30, 20, 10]




# List
my_list = [10, 20, 30]
my_list[0] = 100  # Allowed

# Tuple
my_tuple = (10, 20, 30)
# my_tuple[0] = 100  # TypeError

# SET(remove duplicates)
numbers = {10, 20, 20, 30, 30, 40}
print(numbers)

# Check set operations
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 & set2)  # Intersection
# print(set1 | set2)  # Union
# print(set1 - set2)  # Difference



student = {
    "name": "Devansh",
    "age": 20,
    "branch": "AIML"
}

for key, value in student.items():
    print(key, ":", value)