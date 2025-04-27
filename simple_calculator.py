num1= float(input("enter first number: "))
num2= float(input("enter second number: "))
operation= input("choose operation(+,-,*,/): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    print("Invalid operation selected!")
    result= None 
if result is not None:
    print(f"Result: {num1} {operation} {num2} = {result}")