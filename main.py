from question_model import Question
from data import GiveQuestionData
from quiz_brain import QuizBrain
from ui import Ui

Data = GiveQuestionData()

question_bank = []
for question in Data.QuestionBank:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
Interface = Ui(quiz)