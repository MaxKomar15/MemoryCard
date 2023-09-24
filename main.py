from random import choice, shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QMessageBox, QLabel, QVBoxLayout

app = QApplication([])

from card_window import *

class Question:
    current = None
    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

q1 = Question("Собака", "Dog", "Hot-Dog", "Tog", "Dok")
q2 = Question("Холодильник", "frige", "Fritqe", "trich","fritch")
q3 = Question("Кіт", "Cat", "Kat", "Cad", "Dad")
q4 = Question("Вікно", "window", "vindow", "findow", "Hindow")

questions = [q1, q2, q3, q4]

main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 500)
main_win.move(300, 150)
main_win.setLayout(main_line)


def new_question():
    Question.current = choice(questions)
    question.setText(Question.current.question)
    right_lb.setText(Question.current.right_answer)

new_question()
def click_btn():
    if  answer_btn.text() == "Відповісти":
        group_box.hide()
        answer_box.show()
        answer_btn.setText("Наступне питання")
    else:
        answer_box.hide()
        group_box.show()
        answer_btn.setText("Відповісти")
        new_question()

answer_btn.clicked.connected(click_btn)

main_win.show()
app.exec_()


