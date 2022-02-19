from data import question_data
from question_model import Question_model
from quiz import Quizz_session

quizz_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question_model(question_text, question_answer)
    quizz_bank.append(new_question)

quizz = Quizz_session(quizz_bank)
while quizz.still_have_questions():
    quizz.next_question()
