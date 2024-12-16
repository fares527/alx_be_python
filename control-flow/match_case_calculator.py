

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operat = input("Choose the operation (+, -, *, /): ")

match operat:
    case "+":
        result = num1 + num2
        print("the result is", result) 

    case "-":
        print("the result is", str(num1 - num2))

    case "*":
        print("the result is", str(num1 * num2))

    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            print("the result is", str(num1 / num2))
    