import os
import platform


def main():
    inp = input("Please type 'yes': ")
    if inp.lower() == "yes":
        clear_terminal()


def clear_terminal() -> None:
    # Check if the platform is windows or something else
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
