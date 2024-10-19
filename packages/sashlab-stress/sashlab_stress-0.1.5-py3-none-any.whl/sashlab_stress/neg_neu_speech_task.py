import keyboard as kb
from datetime import datetime, timedelta
from random import choice
from .Participant import Participant, MakeParticipant

NEG_WORDS = [
    "Abuse", "Accident", "Afraid", "Agony", "Annoy", "Murderer", "Stress", 
    "Bankrupt", "Ambulance", "Angry", "Nightmare", "Blackmail", "Bloody", 
    "Bomb", "Crash", "Tragedy", "Victim", "Danger", "Despise", "Destroy", 
    "Rejected", "Disaster", "Unfaithful", "Divorce", "Drown", "Pain", 
    "Evil", "Fear", "Fight", "Fire", "Flood", "Poison", "Guilty", "Gun", 
    "Hate", "Horror", "Hostage", "Panic", "Rude", "Jealousy"
]


NEU_WORDS = [
    "Ankle", "Paint", "Basket", "Jelly", "Windmill", "Book", "Bowl", 
    "Building", "Butter", "Cabinet", "Cat", "Chair", "Clock", "Cow", 
    "Curtains", "Detail", "Door", "Egg", "Elbow", "Elevator", "Engine", 
    "Month", "Farm", "Foot", "Fork", "Frog", "Fur", "Glass", "Golfer", 
    "Kettle", "Hairdryer", "Window", "Hand", "Hat", "Hay", "Headlight", 
    "History", "Horse", "Ink", "Lawn"
]


def main():
    p = MakeParticipant()
    rounds:list[dict]|None = neg_neu_speech(p,0, 60)
    if rounds:
        for round in rounds:
            print(round)
            




def neg_neu_speech(participant:Participant, condition:int, time_limit:int ):
    if condition not in [0, 1]:
        raise ValueError("Condition can only be '0'(negative) or '1'(neutral).")
    elif condition == 0:
        words = NEG_WORDS
    elif condition == 1:
        words = NEU_WORDS

    task_start = datetime.now()
    round = 1
    rounds = []
    
    while True:
        if not (datetime.now() - task_start) >= timedelta(
            seconds=time_limit
        ):
            try:
                word = choice(words)
                print("#############")
                print(word)
                print("#############")

                start = datetime.now()
                kb.wait(hotkey='spacebar')
                duration = (datetime.now() - start)
                rounds.append({'Round':round, 'Prompt': word, 'Duration': duration})
                words.remove(word)
            except KeyboardInterrupt as e:
                print('finish testing')
                rounds.append({'Round':round, 'Prompt': word, 'Duration': duration})
                return rounds
            except Exception as e:
                print(f"{e}")
        else:
            return rounds

if __name__ == '__main__':
    main()
