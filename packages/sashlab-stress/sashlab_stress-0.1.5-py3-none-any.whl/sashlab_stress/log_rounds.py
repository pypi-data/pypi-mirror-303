from .RoundInfo import Round
from .Participant import MakeParticipant, Participant
from .difficulty_manager import DifficultyManager
from datetime import datetime, timedelta
from time import sleep
import pathlib as pl
import csv


def main():
    print("testin' loggin'")
    start = datetime.now()
    d = DifficultyManager()
    sleep(3)
    r1 = Round(1, d.difficulty, (start - datetime.now()))
    sleep(3)
    r2 = Round(2, d.difficulty, (start - datetime.now()))
    p = MakeParticipant()
    log_mental_subtraction_session(p, [r1, r2])


def log_mental_subtraction_session(
    participant: Participant, data: list[Round], path: pl.Path = pl.Path().cwd()
):
    with open(path / f"{participant.id}.csv", mode="w", newline="") as file:
        participant_writer = csv.DictWriter(
            file, fieldnames=participant.to_dict().keys()
        )
        participant_writer.writeheader()
        participant_writer.writerow(participant.to_dict())

        file.write("\n\n")

        data_writer = csv.DictWriter(file, fieldnames=data[0].to_dict().keys())
        data_writer.writeheader()
        for row in data:
            data_writer.writerow(row.to_dict())


def log_nef_neu_speech_session(
    participant: Participant, data: list[dict[str, int|timedelta|str]], path: pl.Path = pl.Path().cwd()
):
    with open(path / f"{participant.id}.csv", mode="w", newline="") as file:
        participant_writer = csv.DictWriter(
            file, fieldnames=participant.to_dict().keys()
        )
        participant_writer.writeheader()
        participant_writer.writerow(participant.to_dict())

        file.write("\n\n")

        data_writer = csv.DictWriter(file, fieldnames=data[0].keys())
        data_writer.writeheader()
        for row in data:
            data_writer.writerow(row)


if __name__ == "__main__":
    main()
