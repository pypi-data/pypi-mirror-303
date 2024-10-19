import argparse
from .mental_subtraction import mental_subtraction
from .neg_neu_speech_task import neg_neu_speech
from .session_setup import session_setup
from .clear_prompt import clear_terminal
from .log_rounds import log_mental_subtraction_session, log_nef_neu_speech_session
import pathlib as pl


def main():
    clear_terminal()
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Run the app with optional parameters."
    )
    parser.add_argument(
        "--task-type",
        type=str,
        default="mental-subtraction",
        help="The kind of task, ie. the mental subtraction task or the negative/neutral speech task",
    )
    parser.add_argument(
        "--time-limit",
        type=int,
        default=300,
        help="Time limit for the session in seconds",
    )
    parser.add_argument(
        "--trial-time",
        type=int,
        default=15,
        help="Number of seconds before each individual trial timesout from a lack of interaction",
    )
    parser.add_argument(
        "--path",
        type=pl.Path,
        default=pl.Path().cwd(),
        help="The path where the session data will be saved",
    )
    parser.add_argument(
        "--condition",
        type=int,
        default=0,
        help="The condition of the speech task 0 = Negative, 1 = Neutral",
    )
    args = parser.parse_args()

    participant = session_setup(time_limit=args.time_limit, trial_time=args.trial_time)

    if participant:
        print(f"Participant ID: {participant.id}")
        print(f"Attention Check Failures: {participant.attention_fails}")
        if args.task_type == "mental-subtraction":
            rounds = mental_subtraction(
                participant, time_limit=args.time_limit, trial_time=args.trial_time
            )
            if rounds:
                log_mental_subtraction_session(participant, rounds, args.path)
        elif args.task_type == "neg-neu-speech":
            rounds = neg_neu_speech(participant, args.condition, args.time_limit) 
            log_nef_neu_speech_session(participant, rounds, args.path)
        else:
            raise ValueError("""The only available tasks are the mental subtraction task ('mental-subtraction') or the Negative/Neutral speech task ('neg-neu-speech')""")


if __name__ == "__main__":
    main()
