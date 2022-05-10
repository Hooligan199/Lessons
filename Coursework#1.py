import random


def input_data():
    print(game_dict.values())
    user_data = input(">>>").lower()
    if user_data in game_dict.values():
        machine_choice(user_data)
    else:
        print(f"Invalid input {user_data}")
        print("Your choice (rock paper scissors lizard spock)?")
        repeater()


def machine_choice(user_data: str):
    random_number = random.randint(1, 5)
    machine_pick = game_dict[random_number]
    print(machine_pick)

    if machine_pick in winning_combinations[user_data]:
        print("Player WIN!")
        return repeater()
    else:
        print("Computer WIN!")
        return repeater()


def repeater():
    repeater_answer = input("Repeat (Y/N)? :")
    if repeater_answer.lower()[0] == "y":
        input_data()
    elif repeater_answer.lower()[0] == "n":
        pass


if __name__ == '__main__':
    game_dict = {1: "rock", 2: "paper", 3: "scissors", 4: "lizard", 5: "spock"}
    winning_combinations = {"rock": ["lizard", "scissors"],
                            "paper": ["rock", "spock"],
                            "scissors": ["paper", "lizard"],
                            "lizard": ["spock", "paper"],
                            "spock": ["scissors", "rock"]
                            }
    input_data()

