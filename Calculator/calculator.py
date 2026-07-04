def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==o:
        return "Error: Division by zero "
    return x/y

print("===Simple calculator===")
print("1.Add(+)")
print("2. Substract (-)")
print("3.Multiply (*)")
print("4.Divide(/)")

op  = input("Enter the choice (+,-,*,/):")
a = float(input("Enter the first number :"))
b = float(input("Enter the second number:"))
if op == '+':
    result = add(a , b)
elif op == "-":
    result = substract(a, b)
elif op == '*':
    result = multiply(a, b)
elif op == '/':
    result = divide(a, b)
else :
    result = "Invalid operator"
print("Result :", result )