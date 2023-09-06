from questions import question_data
from decide_result import check
from os import system

class DataModel:
    total=0
    index=0
    my_score=0
    QUIZ_OVER=False
    def I_know_when_to_make_process_down(self):
        if self.index>=len(question_data):
            self.QUIZ_OVER=True
    def print_question(self):
        self.total+=1
        print(f"Q {self.index+1} : ",question_data[self.index]["text"],"\t\t\tNOTE: True or False\n\n")
        if check(input("Answer : ").lower().strip(),question_data[self.index]["answer"]):
            self.my_score+=1
            print("Congratulations!. Your answer is true\n")
            print(f"Score : {self.my_score}/ {self.total}")
        else:
            print("Wrong answer")
            print(f"Score : {self.my_score}/ {self.total}")
        system("pause")
        system("cls")
        
        