a = float(input())
operator = input()
b = float(input())

if operator == "+":
    print(a + b)

if operator == "-":
    print(a - b)

if operator == "*":
    print(a * b)

if operator == "/":
    if b != 0:
        print(a / b)
    if b == 0:
        print("Nie można dzielić przez zero")