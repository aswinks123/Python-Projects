#Quizz Game using OOP concept
#Created by Aswin ks


from question_model import Question
from data import question_data
from quizz_brain import Quizz

question_bank=[]


for question in question_data:
    question_text=question['text']
    question_answer=question['answer']

    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Quizz(question_bank)
#quiz.next_question()


while quiz.still_has_question():
    quiz.next_question()

print("Congratulation.You completed the Quizz")
print(f"Your Final score is {quiz.score}/{len(question_bank)}")
