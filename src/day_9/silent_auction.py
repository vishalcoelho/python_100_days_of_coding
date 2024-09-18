import os

BANNER = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''


def render_banner() -> None:
    """Render the game screen on each loop

    :returns None:
    """
    _ = os.system("clear")
    print(BANNER)


def silent_auction() -> str:
    """Conduct a silent auction and return the name of the winning bidder"""

    name_bid = {}
    while True:
        render_banner()
        print("Welcome to the secret auction program")
        name = input("What is your name?: ")
        bid = input("What is your bid? $")
        name_bid[name] = bid
        more = input("Are there any other bidders? Type 'yes' or 'no': ")
        if more == "no":
            break

    curr_high_bid = 0
    max_bidder = ""
    for name in name_bid:
        if int(name_bid[name]) > curr_high_bid:
            curr_high_bid = int(name_bid[name])
            max_bidder = name

    print(f"The winner is {max_bidder} with a bid of ${name_bid[max_bidder]}")
    return max_bidder


if __name__ == "__main__":
    silent_auction()
