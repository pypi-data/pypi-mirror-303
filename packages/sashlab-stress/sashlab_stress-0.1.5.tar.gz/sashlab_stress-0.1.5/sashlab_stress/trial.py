from .make_number import make_number
from inputimeout import inputimeout, TimeoutOccurred


def main():
    print("Let's run a trial")
    result = trial()
    print(result)


def trial(difficulty: int = 2, n_seconds: int = 15) -> bool:
    if difficulty < 2:
        raise ValueError("Difficulty must be greater than 2")
    x_val = make_number(difficulty)
    y_val = make_number(difficulty - 1)

    prompt = f"You have {n_seconds} seconds to solve: {x_val} - {y_val}: \n"

    while True:
        try:
            user_input = inputimeout(prompt=prompt, timeout=n_seconds)
            answer = int(user_input)
            break  # Exit the loop when a valid input is received
        except TimeoutOccurred:
            print("Time's up!")
            return False
        except ValueError:
            print("Please only type numeric characters, e.g., '4'")

    return answer == x_val - y_val


if __name__ == "__main__":
    main()
