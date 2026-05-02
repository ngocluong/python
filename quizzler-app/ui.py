THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
import tkinter as tk

class QuizApp:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=15)

        true_img = tk.PhotoImage(file="images/true.png")
        self.true_btn = tk.Button(image=true_img, highlightthickness=0, command=self.true_press)
        self.true_btn.grid(row=2, column=0)

        false_img = tk.PhotoImage(file="images/false.png")
        self.false_btn = tk.Button(image=false_img, highlightthickness=0, command=self.false_press)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="DONE")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
