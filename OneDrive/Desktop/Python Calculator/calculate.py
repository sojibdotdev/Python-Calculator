def calculate():
    while True:
        equation = input("Enter equation (or 'exit' to quit): ")
        if equation.lower() == 'exit':
            print("Exiting calculator.")
            break
        try:
            # eval function will handle +, -, *, /, and other operations
            result = eval(equation)
            print(f"Result: {result}")
        except:
            print("Invalid input. Please try again.")

calculate()
