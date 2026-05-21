num1 = 0
num2 = 0
operator = ""
run = True

def add():
    return num1 + num2
def subtract():
    return num1 - num2
def multiply():
    return num1 * num2
def divide():
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"
    
def wait():
    print("Press Enter to start again and type 'quit' to exit...")
    user_input = input("# ")
    if user_input == "quit":
        quit()

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print("**********************************************")

def Nline():
    print("\n")

def title():
    line()
    print("Welcome to the Simple Calculator")
    line()

def start():
    clear()
    title()

def restart():
    start()
    main()

def main():
    global num1, num2, operator
    start()
    Nline()
    num1 = float(input("Enter the first number: "))
    Nline()
    operator = input("Enter the operator (+, -, *, /): ")
    Nline()
    num2 = float(input("Enter the second number: "))
  
    
    if operator == "+":
        print("Result:", add())
        wait()
    elif operator == "-":
        print("Result:", subtract())
        wait()
    elif operator == "*":
        print("Result:", multiply())
        wait()
    elif operator == "/":
        print("Result:", divide())
        wait()
    else:
        print("Invalid operator")
        wait()

    
while run: 
    main()
