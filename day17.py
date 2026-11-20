import heapq

numbers = [40, 10, 30, 20, 50]

heapq.heapify(numbers)

print(numbers)



smallest = heapq.heappop(numbers)
print(smallest)




import heapq

numbers = [40, 10, 30, 20, 50]

max_heap = []

for num in numbers:
    heapq.heappush(max_heap, -num)

largest = -heapq.heappop(max_heap)

print(largest)


