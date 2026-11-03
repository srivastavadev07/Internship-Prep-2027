numbers = [10, 20, 30, 40, 50]
for num in numbers:
    print(num)


numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(numbers[i])



numbers = [12, 5, 28, 9, 17]
target = 28
for num in numbers:
    if num == target:
        print("Found!")
        break



numbers = [12, 5, 28, 9, 17]
target = 50
found = False
for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Element found")
else:
    print("Element not found")



numbers = [1, 2, 2, 3, 2, 4, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)



numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)