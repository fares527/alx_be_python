def perform_operation():
    num1 =float(input("Enter your first number: "))
    num2 =float(input("Enter your second number: "))
    operation =input("Enter your operation (add, subtract, multiply, divide): ").lower()

    if operation== add:
        print(num1 + num2)
    if operation== subtract:
        print(num1 - num2)
    if operation== multiply:
        print(num1 * num2)
    if operation== divide:
        if num2 ==0:
            print("cant divide by zero")
        print(num1 / num2)

