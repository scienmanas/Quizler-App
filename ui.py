from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT = ("Ariel",10,"normal")

class Ui:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20)
        self.window.config(bg=THEME_COLOR)
        
        # Label
        
        self.Score = Label(text=f"Score: 0",font=FONT)
        self.Score.config(bg=THEME_COLOR,highlightthickness=0,fg="white")
        self.Score.grid(row=0,column=0,columnspan=2)
        
        # Canvas
        
        self.canvas = Canvas(width=350,height=300)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=50,pady=50)
        self.TextToWrite = self.canvas.create_text(175,150,text="Text Will be inserted here", font=("Ariel",20,"italic"),width=345)
        
        # Buttons
        
        img_1 = PhotoImage(file=r"Python_Course\day 34\Quizler App\images\true.png")
        self.Correct = Button(image=img_1,bg=THEME_COLOR,highlightthickness=0,command=self.CorrectFn)
        self.Correct.grid(row=2,column=0)
        
        img_2 = PhotoImage(file=r"Python_Course\day 34\Quizler App\images\false.png")
        self.Wrong = Button(image=img_2,bg=THEME_COLOR,highlightthickness=0,command=self.WrongFn)
        self.Wrong.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.TextToWrite,text=q_text)
        else :
            self.canvas.itemconfig(self.TextToWrite, text="You have reached the end of the quiz")
            self.Correct.config(state="disabled")
            self.Wrong.config(state="disabled")
       
    def CorrectFn(self):
        self.GiveFeedback(self.quiz.check_answer("True"))
        
    def WrongFn(self):
        self.GiveFeedback(self.quiz.check_answer("False"))
    
    def GiveFeedback(self,check):
        if check:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.Score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)