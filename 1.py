student = {"name": "John", "age": 20}
print(student)

colors = ("Red", "Green", "Blue")
print(colors)

numbers_set = {10, 20, 30, 40}
print(numbers_set)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))

num = int(input("Enter a number to check palindrome: "))
reverse_num = int(str(num)[::-1])

if num == reverse_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")