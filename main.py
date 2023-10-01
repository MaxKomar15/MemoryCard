from PyQt5.QtCore import Qt
from time import sleep
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import choice, shuffle

app = QApplication([])

from card_window import:
from menu_window import:

from card_window import*
class Question:
    current = None
    count_right = 0
    count_wrong = 0


    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def got_right(self):
        Question.count_ans += 1
        Question.count_right += 1

    def got_wrong(self):
        Question.count_ans += 1

q1 = Question('Людина', 'people', 'peple', 'lubunna', 'neger')
q2 = Question("Комп'ютер", 'computer', 'Lapton', 'comp', 'comlp')
q3 = Question('число', 'number', 'nomer', 'chuslo', 'calm')
questions = [q1,q2, q3]
radio_buttons = [btn1, btn2, btn3, btn4]




main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 500)
main_win.move(150, 100)
main_win.setLayout(main_line)

def new_qustion():
    Question.current = choice(questions)
    question.setText(Question.current.question)
    right_lb.setText(Question.current.right_answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(Question.current.right_answer)

    radio_buttons[1].setText(Question.current.wrong_answer1)
    radio_buttons[2].setText(Question.current.wrong_answer2)
    radio_buttons[3].setText(Question.current.wrong_answer3)

    

new_qustion()

def check_result():
    radio_group.setExclusive(False)
    if radio_buttons[0].isChecked():
        Question.count_right()
        result_lb.setText("Правильно")
        radio_group[0].isChecked(False)
    else:
        Question.count_wrong()
        result_lb.setText("Неправильно")

    radio_group.setExclusive(True)


def click_btn():
    if answer_btn.text() == "Відповісти":
        check_result()
        group_box.hide()
        answer_box.show()
        answer_btn.setText("Наступне питання")
    else:
        answer_box.hide()
        group_box.show()
        answer_btn.setText("Відповісти")
        new_qustion()

answer_btn.clicked.connect(click_btn)

def relax():
    pause_time = int(time_box.value()) * 60
    main_win.hide()
    sleep(pause_time)
    main_win.show()

def menu_show():
    main_win.hide()
    count_ans_lb.setText(f"Кількісь відповідей:(Question.count_ans)")
    count_right_lb.setText(f"Кількісь відповідей:(Question.count_right)")
    secess_lb.setText(f"Успішність: {2/4*100}")
    menu_win.show()
    
answer_btn.clicked.connect(relax)
sleep_btn.clicked.connect(relax)
menu_btn.clicked.connect(menu_show)

main_win.show()
app.exec_()