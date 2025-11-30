
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        if operation == "+":
         operation = num1 + num2
         print("The result is "+ str(operation))
    case "-":
        if operation == "-":
         operation = num1 - num2
         print("The result is "+ str(operation))
    case "*":
        if operation == "*":
         operation = num1 * num2
         print("The result is "+ str(operation))
    case "/":
        if num2 == 0:
           print("Cannot divide by zero.")
        elif operation == "/":
         operation = num1 / num2
         print("The result is "+ str(operation))
    case _:
        print("Invalid data type entered.")
    
      