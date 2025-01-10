import os
import msvcrt

BANNER = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|

[ESC] to quit after any calculation completes
"""


def render_banner() -> None:
    """Render the banner on each loop

    :returns None:
    """
    _ = os.system("clear")
    print(BANNER)


def calculator() -> float:
    """Run a calculator program"""

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    op_string = [op for op in operations]

    result = 0
    while True:
        render_banner()
        operand_1 = float(input("What's the first number?: "))
        keep_going = True
        while keep_going:
            print(op_string)
            operation = input("Pick an operation: ")
            operand_2 = float(input("What's the next number?: "))
            if operation in operations:
                result = operations[operation](a=operand_1, b=operand_2)
            print(result)
            prompt = input(
                "Continue with the result [y] or start a new calculation [n], or quit[q]:"
            )
            keep_going = True if prompt == "y" else False
            if keep_going == True:
                operand_1 = result
            else:  # 'n' or any other key press
                if prompt != "q":
                    # Reset result if user doesnt want to quit.
                    result = 0
                break

        if wait_for_esc() is True or prompt == "q":
            # Quit the main loop on ESC or 'q'
            break

    return result


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def sub(a, b):
    return a - b


def wait_for_esc() -> bool:
    """Short loop that waits for escape"""
    for _ in range(10, 0, -1):
        # Note: mscvrt.getch() returns bytes while ch(27) is a string (unicode),
        # you need to decode the keyboard entry before comparing them
        if msvcrt.kbhit() and msvcrt.getch().decode() == chr(27):
            return True

    return False


if __name__ == "__main__":
    calculator()
