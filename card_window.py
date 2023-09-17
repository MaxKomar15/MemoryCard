from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QMessageBox, QLabel, QVBoxLayout, QPushButton, QSpinBox

menu_btn = QPushButton("Меню")
sleep_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_box.setValue(30)

time_lb = QLabel("хвилин")

line1 = QHBoxLayout()
line1.addWidget(menu_btn)
line1.addStretch(1)
line1.addWidget(sleep_btn)
line1.addWidget(time_box)
line1.addWidget(time_lb)

question = QLabel("Яблуко")

btn1 = QRadioButton("apply")
btn2 = QRadioButton("apple")
btn3 = QRadioButton("appla")
btn4 = QRadioButton("applu")

group_box = QGroupBox("Варіанти відповідей:")
radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)


col1 = QHBoxLayout()
col2 = QHBoxLayout()
line2 = QHBoxLayout()

col1.addWidget(btn1)
col1.addWidget(btn2)
col1.addWidget(btn3)
col1.addWidget(btn4)

line2.addLayout(col1)
line2.addLayout(col2)
group_box.setLayout(line2)

answer_btn = QPushButton("Відповісти")

main_line = QVBoxLayout()
main_line.addLayout(line1, stretch=1)
main_line.addWidget(question, alignment=Qt.AlignCenter, stretch=2)
main_line.addLayout(group_box, stretch=8)
main_line.addLayout(answer_btn, stretch=3)