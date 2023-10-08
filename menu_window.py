from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QMessageBox, QWidget, QLabel, QPushButton, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup

menu_win = QWidget("Memory Card Menu")
menu_win.setWindowTitle("Memory Card Menu")
menu_win.resize(400,200)
menu_win.move(200, 200)

stat_lb = QLabel("Статистика")
stat_lb.setStyleSheet('font-size: 19px; font-weight: bold;'')
                      
count_ans_lb = QLabel("Кількість відпвідей: 0")
count_right_lb = QLabel("Кількість правильних відповідей: 0%")
succes_lb = =QLabel("Успішність: 0")

vline = QVBoxLayout()
vline.addWidget(stat_lb)
vline.addWidget(count_ans_lb)
vline.addWidget(count_right_lb)
vline.addWidget(succes_lb)

menu_win.setLayout(vline)

                    
