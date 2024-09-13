import os

BANNER = """
 .--.
:
|    .-.  .-. .--. .-.  .--.
:   (   )(.-' `--.(   ) |
 `--'`-'`-`--'`--' `-'`-'
 .--.          .
:      o       |
|      .  .,-. |--. .-. .--.
:      |  |   )|  |(.-' |
 `--'-' `-|`-' '  `-`--''
          |
          '
"""


def render_banner() -> None:
    """Render the game screen on each loop

    :returns None:
    """
    _ = os.system("clear")
    print(BANNER)


def encode(text: str, shift: int) -> str:
    """Function to encode plain text based on the shift provided

    :param text: original plaint text
    :param shift: numerical shift in the alphabet
    :returns: ciphertext
    """
    ciphertext = []
    for ch in text:
        shift_ch = ord(ch) + shift
        if shift_ch > ord("z"):
            shift_ch -= 26
        elif shift_ch < ord("a"):
            shift_ch += 26
        else:
            pass
        ciphertext.append(chr(shift_ch))

    return "".join(ciphertext)


def decode(text: str, shift: int) -> str:
    """Function to decode cipher text based on the shift provided

    :param text: cipher text
    :param shift: numerical shift in the alphabet
    :returns: plaintext
    """
    return encode(text, -shift)


def caesar_cipher() -> str:
    """Encode or decode strings using the caesar cipher"""
    render_banner()
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ret = ""
    if direction == "encode":
        ret = encode(text, shift)
    elif direction == "decode":
        ret = decode(text, shift)
    else:
        pass

    print(ret)

    return ret


if __name__ == "__main__":
    caesar_cipher()
