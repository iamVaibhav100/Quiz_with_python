class QuizBrain:
    def __init__(self, q_list):
        self.que_no = 0
        self.score = 0
        self.que_list = q_list

    def still_has_que(self):
        return self.que_no < len(self.que_list)

    def next_question(self):
        current_que = self.que_list[self.que_no]
        self.que_no += 1
        user_ans = input(f"Q.{self.que_no}: {current_que.que}? (True/False): ")
        self.check_ans(user_ans, current_que.ans)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("Absolutely right!")
        else:
            print("Boo! wrong answer")
        print(f"correct answer: {correct_ans}")
        print(f"Your score: {self.score}/{self.que_no}")
        print("\n")
