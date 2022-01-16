class Quizz_session:
    def __init__(self, quizz_list):
        self.quizz_list = quizz_list
        self.score = 0
        self.question_number = 0

    def still_have_questions(self):
        if self.question_number < len(self.quizz_list):
            return True
        else:
            print("Great,you have completed the quizz.")
            print(f"Your final score is {self.score}/{self.question_number}")
            return False 


    def next_question(self):
        current_question = self.quizz_list[self.question_number]
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)
        print(f"Your score is {self.score}/ {self.question_number}")
        print("\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Great, that´s correct!")
            self.score += 1 
        else:
            print("Sorry, that´s not correct!")
        print(f"Correct answer was {correct_answer}")






    
