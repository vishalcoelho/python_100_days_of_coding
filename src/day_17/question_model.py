"""Question class"""


class Question:
    """A question class"""

    def __init__(self, text: str, answer: str) -> None:
        self.text = text
        self.answer = answer


# ================================TEST=========================================
if __name__ == "__main__":
    question = Question("2+3=?", "5")
