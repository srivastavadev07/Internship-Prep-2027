# O(1) — Constant Time
numbers = [10, 20, 30, 40, 50]
print(numbers[0])

    # O(n) — Linear Time
numbers = [10, 20, 30, 40, 50]
for n in numbers:
    print(n)

    # O(n²) — Quadratic Time
numbers = [10, 20, 30, 40, 50]
for n in numbers:
    for m in numbers:
        print(n, m)




# numbers = [10, 20, 30, 40, 50]
# target = 30
# for i in range(len(numbers)):
#     if numbers[i] == target:
#         print("Found at index:", i)
#         break



numbers = [10, 20, 30, 40, 50, 60, 70]

target = 50

low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found at index:", mid)
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1


    
numbers = [5, 3, 8, 1, 2]

n = len(numbers)

for i in range(n):
    for j in range(n - i - 1):

        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)