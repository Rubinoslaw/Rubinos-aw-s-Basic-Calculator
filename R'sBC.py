# Rubinosław's Basic Calculator

num_1 = float(input("Please insert the first number: "))
num_2 = float(input("Please insert the second number: "))

operation = input("Please choose an operation: ")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")

if operation == "1":
    result = num_1 + num_2
    print(result)
elif operation == "2":
    result = num_1 - num_2
    print(result)
elif operation == "3":
    result = num_1 * num_2
    print(result)
elif operation == "4":
    result = num_1 / num_2
    if num_2 != 0:
        print(result)
    else:
        print("Error: You cannot divide by 0!")
elif operation == "5":
    result = num_1 ** num_2
    print(result)
else:
    print("Invaild operation!")
