# def greet():
#     print("Hello, bro!")

# greet()
# greet()



# def greet(name):
#     print("Hello,", name)

# greet("Devansh")
# greet("Rahul")
# greet("Aman")




# def greet(name="bro"):
#     print("Hello,", name)

# greet()
# greet("Devansh")



def fact(num):
    i = 1
    factorial = 1
    while i <= num:
        factorial *= i
        i += 1
    return factorial

print(fact(4))
