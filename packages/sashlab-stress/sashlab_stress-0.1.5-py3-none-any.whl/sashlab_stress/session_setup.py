from .Participant import Participant, MakeParticipant
from .attention import attention_check
import time
import winsound


def session_setup(time_limit: int, trial_time: int) -> Participant | None:
    print("Session set up:")
    print(f"Session duration: {time_limit/60} minutes")
    print(f"Trial timeout limit: {trial_time}")
    try:
        participant: Participant = MakeParticipant()

        attention_counter = 0
        while not attention_check() and attention_counter < 5:
            attention_counter += 1
            if attention_counter >= 5:
                print("You have failed the attention check too many times")
                time.sleep(1)
                winsound.Beep(880, 2200)
                break

        participant.set_attention_fails(attention_counter)

        return participant
    except Exception as e:
        print(f"Could not set up session: {e}")
        return None
