import math

while True:
    print("\nScientific Calculator")
    print("1. Square Root")
    print("2. Factorial")
    print("3. Natural Log")
    print("4. Power")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = float(input("Enter number: "))
        print("Square Root:", math.sqrt(x))

    elif choice == 2:
        x = int(input("Enter number: "))
        print("Factorial:", math.factorial(x))

    elif choice == 3:
        x = float(input("Enter number: "))
        print("Natural Log:", math.log(x))

    elif choice == 4:
        x = float(input("Enter base: "))
        y = float(input("Enter power: "))
        print("Power:", math.pow(x,y))

    elif choice == 5:
        break
