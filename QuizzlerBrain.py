from html import unescape



class QuizBrain:

    def __init__(self, questionbank):
        self.score = 0
        self.questionnumber = 0
        self.categorynumber = 0
        self.questionlist = questionbank

    def hasquestions(self):
        '''Checks if there is still questions to ask or not.'''

        return self.questionnumber < len(self.questionlist)

    def nextquestion(self):
        '''Asks the next question.'''

        self.question = unescape(self.questionlist[self.questionnumber].question)
        self.correctanswer = self.questionlist[self.categorynumber].answer
        self.questionnumber += 1

        return f'Q.{self.questionnumber}: {self.question}'
        
    def nextcategory(self):
        '''gives next question\'s category'''

        self.category = self.questionlist[self.categorynumber].category
        self.categorynumber += 1

        return f'Category: {self.category}'

    def checkanswer(self, useranswer):
        '''checks users answer with the correct answer and scores it.'''

        correctanswer = self.correctanswer
        if useranswer.lower() == correctanswer.lower():
            self.score += 1
            return True
        else:
            return False

    def gamescore(self):
        return self.score