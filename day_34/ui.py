from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = ("Arial", 16, "italic")


class QuizGui:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz True or False")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=20, pady=20)
        # Labels
        self.score = Label(text="Score: ", fg="white", font=FONT_NAME)
        self.score.config(bg=THEME_COLOR)
        self.score.grid(column=1, row=0, padx=20, pady=20, sticky="w")
        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            113,
            135,
            width=220,
            text="",
            font=FONT_NAME, fill=THEME_COLOR,
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        # Buttons
        self.check_image = PhotoImage(file="images/true.png")
        self.x_image = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.check_image, command=self.select_true_answer)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = Button(image=self.x_image, command=self.select_false_answer)
        self.wrong_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def select_true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def select_false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text= f"Score: {self.quiz.score}" )
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="No more questions.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_question)



