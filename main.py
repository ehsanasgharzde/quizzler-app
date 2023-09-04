# ---------------------------- LIBRARIES ------------------------------- #
from QuizzlerBrain import QuizBrain
from QuestionModel import Question
from UISetup import UISetup
from GameData import gamedata


# ---------------------------- CONSTANTS ------------------------------- #
SCORE = 0
QUESTIONBANK = []

# ---------------------------- GETTING QUESTIONS ------------------------------- #
for index in range(0, 10):
    QUESTIONBANK.append(Question(gamedata[index]['question'], 
                                 gamedata[index]['correct_answer'],
                                 gamedata[index]['category']
                                 )
                            )

# ---------------------------- QUIZZLER GAME ------------------------------- #
quizzlerbrain = QuizBrain(QUESTIONBANK)
quizzleruisetup = UISetup(quizzlerbrain)