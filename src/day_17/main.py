from pprint import pprint  # Python built-in
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = [
    Question(q_and_a["text"], q_and_a["answer"]) for q_and_a in question_data
]
# pprint(question_bank)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(
    "You have completed the quiz\n",
    f"Final Score: {quiz_brain.score}/{quiz_brain.question_number}",
)
