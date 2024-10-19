import random as ra


def main():
    n = make_number(int(input("Please enter a number: ")))
    print(n)


def make_number(length: int) -> int | None:
    if length < 1:
        raise ValueError("Cannot make a number less than 1 digit long")

    temp_list: list[int] = []

    try:
        for i in range(length):
            temp_list.append(ra.randint(0, 9))

        wanted_val = int("".join([str(i) for i in temp_list]))
    except ValueError as e:
        raise ValueError("An error occurred while constructing the number") from e

    return wanted_val


if __name__ == "__main__":
    main()
