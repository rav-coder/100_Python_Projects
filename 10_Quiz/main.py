from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question_bank.append(Question(key['question'], key['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz complete!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

# print(question_bank[0].text)
