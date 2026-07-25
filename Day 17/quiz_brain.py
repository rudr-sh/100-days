class QuizBrain:
    def __init__(self,q_list):
        self.q_num=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        question = self.question_list[self.q_num]  
        user_ans=input(f"Q.{self.q_num+1}: {question.text}(True/False)?: ")
        self.check_answer(user_ans)
    def still_has_questions(self):
        return self.q_num<len(self.question_list)
    def check_answer(self,user_ans):
        check= self.question_list[self.q_num]
        if user_ans == check.answer:
            self.score+=1
            print("Correct Answer")            
            print(f"Score:{self.score}")
        else:
            print("Wrong Answer")
            print(f"Score:{self.score}")
        print(f"The correct answer was: {check.answer}")
        print(f"Your score is:{self.score}/{self.q_num+1}")
        print("\n")