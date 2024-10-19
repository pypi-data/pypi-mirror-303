"""In future this should be rebuilt using fastapi, but for right now I don't have the time to learn that fully to impliment it"""

from datetime import datetime
import random as ra
import string


def main():
    test = Participant()
    print(test.__repr__())  # Call the method, not just print the method reference.
    test_dict = test.to_dict()
    for k, v in test_dict.items():
        print(f"{k} = {v}")
    test2 = MakeParticipant()
    print(repr(test2))
    print(type(test2.start_time))


class Participant:
    def __init__(
        self,
        start_time: datetime | None = None,
        id: str | None = None,
        len_id: int = 8,
        attention_fails: int = 0,
    ):
        if not id:
            self.id = "".join(
                ra.choice(string.ascii_letters + string.digits) for _ in range(len_id)
            )
        else:
            self.id = id

        # If start_time isn't provided, default to current time
        self.start_time = start_time if start_time else datetime.now()
        self.attention_fails = attention_fails

    def set_attention_fails(self, fails: int = 0):
        self.attention_fails = fails

    def set_start_time(self):
        self.start_time = datetime.now()

    def __repr__(self) -> str:
        return f"Participant(id={self.id}, start_time={self.start_time})"

    def to_dict(self) -> dict[str, tuple[str, int, datetime, int]]:
        return {
            "id": self.id,
            "len_id": int(len(self.id)),
            "attention_fails": self.attention_fails,
            "start_time": self.start_time,
        }


def MakeParticipant() -> Participant:
    print("Please enter the participant id:")
    participant_id = input("Just press enter to randomly generate an 8 digit id\n:")
    if participant_id.lower().strip() == "":
        particicpant_id = None
        len_participant_id = 0
        print("Partiticipant id will be randomly generated")
        return Participant(id=participant_id)
    else:
        len_participant_id = len(participant_id)
        print(f"Participant id = {participant_id}")
        return Participant(id=participant_id, len_id=len_participant_id)


# might be a good idea to write a MakeParticipant function
# but for right now the constructor is fine.

if __name__ == "__main__":
    main()
