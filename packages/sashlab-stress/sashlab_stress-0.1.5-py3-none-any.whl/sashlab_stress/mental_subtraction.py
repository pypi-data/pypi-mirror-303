from .Participant import Participant, MakeParticipant
from .RoundInfo import Round
from .difficulty_manager import DifficultyManager
from .clear_prompt import clear_terminal
from .trial import trial
import keyboard as kb
from datetime import datetime, timedelta
import time

def main():
    p = MakeParticipant()
    rounds:list[Round]|None = mental_subtraction(p, 60, 10)
    if rounds:
        for round in rounds:
            print(round)

def mental_subtraction(
    participant: Participant, time_limit: int, trial_time: int
) -> list[Round] | None:
    print(
        """
        In the next section subtraction problems will appear on screen. Please solve the problem by entering your answer to the problem and then pressing enter. Ensure to only enter numeric characters.\n

        Press the Spacebar when you're ready to continue
        """
    )

    kb.wait(hotkey="spacebar")
    participant.set_start_time()
    clear_terminal()

    d = DifficultyManager()
    round: int = 1
    rounds: list[Round] = []

    while True:
        clear_terminal()
        if not (datetime.now() - participant.start_time) >= timedelta(
            seconds=time_limit
        ):
            r = Round(round, d.difficulty, (datetime.now() - participant.start_time))
            try:
                print(f"Round {round}")
                print(f"You are playing at difficulty level {d.get_difficulty()-1}")
                answer = trial(d.get_difficulty(), n_seconds=trial_time)
                print(answer)
                d.update_streaks(answer)
                d.update_difficulty()
                r.set_answer(answer)
                round += 1

                time.sleep(1)
            except KeyboardInterrupt:
                print("Finished testing")
                rounds.append(r)
                return rounds
            finally:
                rounds.append(r)

        else:
            if rounds:
                print("This activity is finished")
                return rounds
            else:
                print("This activity is finished")
                return None

if __name__ == '__main__':
    main()
