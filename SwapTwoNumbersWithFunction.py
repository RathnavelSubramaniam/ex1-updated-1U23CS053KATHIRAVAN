def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

x, y = swap_numbers(x, y)

print("After swapping:")
print("x =", x)
print("y =", y)
