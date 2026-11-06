# students = {
#     101: "Rahul",
#     102: "Aman",
#     103: "Priya"
# }
# print(students[102])



student = {
    "name": "Dev",
    "age": 20,
    "branch": "AIML"
}
print(student["name"])
student["age"] = 21
student["college"] = "Engineering College"
print(student)



numbers = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)




numbers = [2, 7, 11, 15]
target = 9
seen = {}
for i in range(len(numbers)):
    complement = target - numbers[i]
    if complement in seen:
        print([seen[complement], i])
        break
    seen[numbers[i]] = i