import pyfiglet
from termcolor import colored
import os
import random

banner_file = "banner.txt"
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']

# Tool banner name (change as you like)
tool_name = "Color Banner Tool"

def show_banner(name):
    ascii_banner = pyfiglet.figlet_format(name)
    color = random.choice(colors)
    print(colored(ascii_banner, color))

def get_username():
    if os.path.exists(banner_file):
        with open(banner_file, "r") as f:
            name = f.read().strip()
        return name
    else:
        # First run: show tool name banner
        show_banner(tool_name)
        # Then ask for user name
        name = input("\nEnter your name or text for the banner: ")
        with open(banner_file, "w") as f:
            f.write(name)
        return name

def update_name():
    name = input("Enter new name or text: ")
    with open(banner_file, "w") as f:
        f.write(name)
    print("Name updated!")

def main():
    if os.path.exists(banner_file):
        print("[1] Show banner\n[2] Change name\n[3] Exit")
        choice = input("Your choice (1/2/3): ")
        if choice == "1":
            name = get_username()
            show_banner(name)
        elif choice == "2":
            update_name()
        else:
            print(colored("Goodbye!", "yellow"))
    else:
        name = get_username()
        show_banner(name)

if __name__ == "__main__":
    main()
