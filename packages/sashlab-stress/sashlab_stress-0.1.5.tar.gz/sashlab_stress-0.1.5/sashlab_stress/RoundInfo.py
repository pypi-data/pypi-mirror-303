from .difficulty_manager import DifficultyManager
from datetime import datetime, timedelta
import time


def main():
    start = datetime.now()
    d = DifficultyManager()
    a = True
    time.sleep(15)
    td = start - datetime.now()
    r = Round(1, d.difficulty, td)
    print(r.to_dict())
    r.set_answer(a)
    print(r.to_dict())


class Round:
    def __init__(
        self,
        n_round: int,
        difficulty: int,
        time: timedelta,
        answer: bool = False,
    ):
        self.n_round = n_round
        self.difficulty = difficulty
        self.answer = answer
        self.time = time

    def set_answer(self, is_correct: bool):
        self.answer = is_correct

    def to_dict(self) -> dict[str, tuple[int | bool | timedelta]]:
        return {
            "Round Number": self.n_round,
            "Difficulty": self.difficulty,
            "Answer": self.answer,
            "Time stamp": self.time,
        }


if __name__ == "__main__":
    main()
