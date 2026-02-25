import os
import msvcrt
import random

BANNER = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""


def render_banner() -> None:
    """Render the banner on each loop

    :returns None:
    """
    _ = os.system("clear")
    print(BANNER)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand_value = 0
dealer_hand_value = 0
prompt_dealer_wins = f"Dealer wins."
prompt_user_wins = f"User wins."
prompt_draw = f"Draw."

def blackjack() -> str:
    """Run a blackjack program"""
    result = ''
    play_again = 'y'
    while play_again == 'y':
        render_banner()
        user_hand = []
        user_hand_value = 0
        dealer_hand = []
        dealer_hand_value = 0

        # Deal a card to the dealer
        add_to_hand(dealer_hand, deal_card())

        # Deal a card to the user
        add_to_hand(user_hand, deal_card())
        show_hand(user_hand, "user")

        # Deal another card to the dealer, check for winning hand
        add_to_hand(dealer_hand, deal_card())
        dealer_hand_value = calculate_hand_value(dealer_hand)

        if dealer_hand_value == 21:
            result = prompt_dealer_wins
        else:
            # Repeatedly ask user to hit or pass, calculate hand value
            while (user_hand_value < 21):
                hit = input("Do you want another card y/n? ")
                if hit == 'y':
                    add_to_hand(user_hand, deal_card())
                    show_hand(user_hand, "user")
                    user_hand_value = calculate_hand_value(user_hand)
                else:
                    break

            # Keep dealing cards to the dealer if hand value < 17
            while (dealer_hand_value < 17):
                add_to_hand(dealer_hand, deal_card())
                dealer_hand_value = calculate_hand_value(dealer_hand)

            # reveal cards, find winner
            print("\nREVEAL!!")
            show_hand(dealer_hand, "dealer")
            show_hand(user_hand, "user")
            if user_hand_value > 21:
                print("BUST!!")
                result = prompt_dealer_wins
            elif dealer_hand_value > 21:
                result = prompt_user_wins
            elif dealer_hand_value == user_hand_value:
                result = prompt_draw
            elif user_hand_value > dealer_hand_value:
                result = prompt_user_wins
            else:
                result = prompt_dealer_wins

        print(result)
        play_again = input("Do you wish to play again y/n? ")
    return result

def deal_card() -> int:
    """Deal a card randomly from the infinite deck"""
    card = random.choice(cards)
    return card

def add_to_hand(hand:list, card:int) -> None:
    """Add a card to a hand"""
    hand.append(card)

def show_hand(hand:list, owner:str) -> None:
    """Display a hand"""
    print(f"{owner}:{hand}")

def calculate_hand_value(hand:list) -> int:
    """Calculate the value of a hand"""
    value = sum(hand)

    # Might have to convert aces from 11 to 1 if hand exceeds 21
    if value > 21:
        for card in hand:
            if card == 11:
                value -= 10
            if value <= 21:
                break;

    return value

if __name__ == "__main__":
    blackjack()
