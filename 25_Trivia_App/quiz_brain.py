import html
from question_model import Question
from data import question_data


class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0

        self.question_list = []
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_list.append(new_question)

        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {q_text} "

    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

        # return f"Score: {self.score}/{self.question_number}"
