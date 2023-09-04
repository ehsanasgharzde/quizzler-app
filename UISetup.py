# ---------------------------- LIBRARIES ------------------------------- #
from tkinter import *
from QuizzlerBrain import QuizBrain

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = '#E9DCBE'
GREEN = '#54E346'
RED = '#F55C47'
BG = '#A4B787'

# ---------------------------- UI SETUP CLASS ------------------------------- #
class UISetup:

    def __init__(self, quizzlerbrain: QuizBrain):
        self.brain = quizzlerbrain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(350, 450)
        self.window.config(bg=BG, padx=25, pady=25)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg=WHITE)
        self.category = self.canvas.create_text(150, 25, text='CATEGORY', font=('Arial', 8, 'normal'))
        self.question = self.canvas.create_text(150, 125, text='QUESTION', font=('Arial', 14, 'italic'), width=280)
        self.canvas.grid(row=0, column=0, columnspan=2, pady=25)

        self.scorelabel = Label(text='Score: 0', bg=BG, font=('Courier', 15, 'bold'))
        self.scorelabel.grid(row=5, column=0, columnspan=2, pady=10)

        trueimg= PhotoImage(file='Images/true.png')
        self.truebutton = Button(image=trueimg, borderwidth=0, bg=BG, activebackground=BG, border=0, command=self.true)
        self.truebutton.grid(row=4, column=0, pady=15)

        falseimg = PhotoImage(file='Images/false.png')
        self.falsebutton = Button(image=falseimg, borderwidth=0, bg=BG, activebackground=BG, border=0, command=self.false)
        self.falsebutton.grid(row=4, column=1, pady=15)

        self.nextquestion()

        self.window.mainloop()

    def nextquestion(self):
        self.canvas.config(bg=WHITE)

        QUESTION = self.brain.nextquestion()
        CATEGORY = self.brain.nextcategory()

        self.canvas.itemconfig(self.question, text=QUESTION)
        self.canvas.itemconfig(self.category, text=CATEGORY)
    
    def true(self):
        self.checkanswer('true')

    def false(self):
        self.checkanswer('false')

    def checkanswer(self, useranswer):
        if self.brain.checkanswer(useranswer):
            self.canvas.config(bg=GREEN)
            self.scorelabel.config(text=f'Score: {self.brain.gamescore()}')
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, func=self.nextquestion)