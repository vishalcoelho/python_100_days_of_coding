from typing import List
from question_model import Question


class QuizBrain:
    """Quiz Brain Class"""

    def __init__(self, question_list: List[Question]) -> None:
        self.question_number = 0
        # Create a generator
        self.question_list = (question for question in question_list)
        # print(type(self.question_list))
        self.score = 0
        self.curr_question: Question = Question("", "")
        self.num_questions = len(question_list)

    def still_has_questions(self) -> bool:
        """Checks if the quiz brain still has questions

        Returns:
            bool: True, if there are more questions, else False
        """
        return self.question_number < self.num_questions

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """Check user's answer against the correct one

        Args:
            user_answer (str): user's answer
            correct_answer (str): expected answer

        Returns:
            None
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")

    def next_question(self) -> None:
        """Display the next question and get the user's answer"""
        self.question_number += 1
        self.curr_question = next(self.question_list)
        answer = input(
            f"Q.{self.question_number}: {self.curr_question.text} (True/False)? "
        )
        self.check_answer(answer, self.curr_question.answer)


# ================================TEST=========================================
from data import question_data  # pylint: disable=wrong-import-position

if __name__ == "__main__":
    quiz_brain = QuizBrain([Question(qa["text"], qa["answer"]) for qa in question_data])
    quiz_brain.next_question()
    quiz_brain.next_question()
    quiz_brain.next_question()
