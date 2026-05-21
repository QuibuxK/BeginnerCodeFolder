import os

run = True
def weight_converter(Choice):
    if choice == '1':
        line()
        pounds = float(input("Enter weight in pounds: "))
        line()
        Nline()
        kilograms = pounds * 0.453592
        print(f"{pounds} pounds is equal to {kilograms:.2f} kilograms.")
    elif choice == '2':
        line()
        kilograms = float(input("Enter weight in kilograms: "))
        line()
        Nline()
        pounds = kilograms / 0.453592
        print(f"{kilograms} kilograms is equal to {pounds:.2f} pounds.")
    elif choice == '3':
        line()
        print("Exiting the weight converter. Goodbye!")
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
    print("Welcome to the weight converter!")
    print("Please select the conversion you would like to perform:")
    print("1. Pounds to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Exit")
    line()
    Nline()

    choice = input("Enter your choice (1/2/3): ")
    clear_screen()

    weight_converter(choice)
    Nline()
    wait()