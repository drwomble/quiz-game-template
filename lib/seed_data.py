from classes.quiz import Quiz

Quiz.drop_table()
Quiz.create_table()

question_1 = Quiz.create('What is 2+2', '4')
question_2 = Quiz.create('What is 5+5', '10')

print('seed data successfully created')