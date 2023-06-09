import sqlite3

CONN = sqlite3.connect('quiz.db')
CURSOR = CONN.cursor()

class Quiz:
    
    def __init__(self, question, answer, id=None):
        self.question = question
        self.answer = answer
        self.id = id
        
    @property
    def question(self):
        pass
    
    @question.setter
    def question(self, question):
        pass
    
    @property
    def answer(self):
        pass
    @answer.setter
    def answer(self):
        pass
    
    @classmethod
    def create_table(cls):
        pass
    
    @classmethod
    def drop_table(cls):
        pass
    
    def save(self):
        pass
    
    @classmethod
    def create(cls, question, answer):
        pass
    
    @classmethod
    def get_all(cls):
        pass
    
    @classmethod
    def find_by_question(cls, question):
        pass