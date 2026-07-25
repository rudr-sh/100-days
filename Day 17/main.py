from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    ques = Question(i["text"],i["answer"])
    question_bank.append(ques)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.q_num+=1
print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.q_num}")
