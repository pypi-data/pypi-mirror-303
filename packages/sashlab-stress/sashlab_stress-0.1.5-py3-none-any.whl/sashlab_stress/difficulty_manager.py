def main():
    d = DifficultyManager()
    print(d.get_difficulty())
    answers = [True, True, True]
    for i in answers:
        d.update_streaks(answers)
    d.update_difficulty()
    print(d.get_difficulty())


class DifficultyManager:
    def __init__(self, difficulty: int = 2):
        self.correct_streak = 0
        self.incorrect_streak = 0
        self.difficulty = (
            difficulty  # Starts at two because of the nature of the trial.py function
        )

    def update_streaks(self, is_correct):
        if is_correct:
            self.correct_streak += 1
            self.incorrect_streak = 0
        else:
            self.incorrect_streak += 1
            self.correct_streak = 0

    def update_difficulty(self):
        if self.correct_streak >= 3:
            self.difficulty += 1
            self.correct_streak = 0
        elif self.incorrect_streak >= 3:
            # Ensure difficulty does not go below 2
            self.difficulty = max(self.difficulty - 1, 2)
            self.incorrect_streak = 0

    def get_difficulty(self):
        return self.difficulty


if __name__ == "__main__":
    main()
