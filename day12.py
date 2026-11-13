stack = []
# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

# View top element
print(stack[-1])

# Remove top element
stack.pop()
print(stack)




# def is_balanced(s):
#     stack = []
#     pairs = {
#         ')': '(',
#         '}': '{',
#         ']': '['
#     }
#     for ch in s:
#         if ch in "({[":
#             stack.append(ch)
#         elif ch in ")}]":
#             if not stack:
#                 return False
#             if stack.pop() != pairs[ch]:
#                 return False
#     return len(stack) == 0
# print(is_balanced("({[]})"))
# print(is_balanced("(]"))