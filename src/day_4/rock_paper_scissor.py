from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
prompt_tie = "Tie!!!"
prompt_win = "You win!!!"
prompt_lose = "You lose!!!"

rps = [rock, paper, scissors]


def rock_paper_scissors() -> str:
    """Classic Rock, Paper, Scissors game"""
    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    )
    comp_choice = randint(0, 2)

    print("You chose:\n" + rps[user_choice])
    print("Computer chose: \n" + rps[comp_choice])

    if comp_choice == user_choice:
        result = prompt_tie
    elif ((comp_choice - user_choice) == 1) or ((comp_choice - user_choice) == -2):
        result = prompt_lose
    else:
        result = prompt_win

    print(result)
    return result


if __name__ == "__main__":
    rock_paper_scissors()
