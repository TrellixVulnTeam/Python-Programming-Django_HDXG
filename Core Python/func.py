def arithimet(a,b):
    """This function finds the sum of tow numbers."""

    # Addition of numbers
    add = a + b

    # Subtraction of numbers
    sub = a - b

    # Multiplication of number
    mul = a * b

    # Division(float) of number
    div1 = a / b

    # Division(floor) of number
    div2 = a // b

    # Modulo of both number
    mod = a % b

    # Power
    p = a ** b

    print("Addition = ", add)
    print("Subtraction = ", sub)
    print("Mul = ", mul)
    print("Division(float) = ", div1)
    print("Division(floor) = ", div2)
    print("Modulo = ", mod)
    print("Power = ", p)

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

arithimet(x,y)