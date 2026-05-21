import os

run = True

def temp_converter(Choice):
    if choice == '1':
        line()
        celsius = float(input("Enter temperature in Celsius: "))
        line()
        Nline()
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == '2':
        line()
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        line()
        Nline()
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C.")
    elif choice == '3':
        line()
        print("Exiting the temperature converter. Goodbye!")
        line()
        Nline()
        wait()
        quit()
    else:
        print("Invalid choice. Please try again.")



def wait():
    input("Press Enter to continue...")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print("-" * 40)

def Nline():
    print("\n")

while run:
    clear_screen()
    line()
    print("Welcome to the temperature converter!")
    print("Please select the conversion you would like to perform:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    line()
    Nline()

    choice = input("Enter your choice (1/2/3): ")
    clear_screen()

    temp_converter(choice)
    Nline()
    wait()