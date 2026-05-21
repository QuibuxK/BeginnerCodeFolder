import os, random
TDS = "NULL"
run = True

overwatch_roles = {
    "Tank": [
        "D.Va",
        "Domina",
        "Doomfist",
        "Hazard",
        "Junker Queen",
        "Mauga",
        "Orisa",
        "Ramattra",
        "Reinhardt",
        "Roadhog",
        "Sigma",
        "Winston",
        "Wrecking Ball",
        "Zarya"
    ],

    "Damage": [
        "Anran",
        "Ashe",
        "Bastion",
        "Cassidy",
        "Echo",
        "Emre",
        "Freja",
        "Genji",
        "Hanzo",
        "Junkrat",
        "Mei",
        "Pharah",
        "Reaper",
        "Sierra",
        "Sojourn",
        "Soldier: 76",
        "Sombra",
        "Symmetra",
        "Torbjörn",
        "Tracer",
        "Vendetta",
        "Venture",
        "Widowmaker"
    ],

    "Support": [
        "Ana",
        "Baptiste",
        "Brigitte",
        "Illari",
        "Jetpack Cat",
        "Juno",
        "Kiriko",
        "Lifeweaver",
        "Lúcio",
        "Mercy",
        "Mizuki",
        "Moira",
        "Wuyang",
        "Zenyatta"
    ]
}

def wait():
    input("Press Enter to continue...")

def quit():
    print("Thanks for using the Overwatch 2 Random Character Picker! Goodbye!")
    wait()
    exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def line():
    print("-" * 50)

def Nline():
    print("\n")

def RandomCharacterPicker(TDS):
    if TDS == "tank" or TDS == "t":
        role = "Tank"
    elif TDS == "damage" or TDS == "d":
        role = "Damage"
    elif TDS == "support" or TDS == "s":
        role = "Support"
    elif TDS == "quit" or TDS == "q":
        quit()
    else:
        role = random.choice(list(overwatch_roles.keys()))
    character = random.choice(overwatch_roles[role])
    print(f"You got {character} from the {role} role!")
    wait()

while run:
    clear()
    line()
    print("Welcome to the Overwatch 2 Random Character Picker! " \
    "Press Enter to get a random character from any role."
    "enter 'tank', 'damage', or 'support' to get a random character from that role. " \
    "Enter 'quit' to exit the program.")
    line()
    Nline()

    TDS = input("What role do you want to play? (Tank, Damage, Support, or Random): ").lower()

    RandomCharacterPicker(TDS)