from question_model import DataModel
from prettytable import PrettyTable


table = PrettyTable()
model=DataModel()


while not model.QUIZ_OVER:
    model.print_question()
    model.index+=1
    model.I_know_when_to_make_process_down()
table.add_column("YOUR SCORE",[f"{model.my_score}"])
table.add_column("TOTAL HURDLES",[f"{model.total}"])
print(table)