first= input("enter your first number?")
second= input("enter your second number?")
operator= input("enter your operator(+, -, *, /, %,<,>)?")
first = int(first)
second= int(second)
if operator== "+":
    print(first+second)
elif operator== "-":
    print(first-second)
elif operator== "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator== "%":
    print(first%second)
elif operator=="<":
    print(first<second)
elif opertor==">":
    print(first>second)
else :
    print("invalid operator")
