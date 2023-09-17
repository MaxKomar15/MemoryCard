from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QMessageBox, QLabel, QVBoxLayout


app = QApplication([])

from card_window import main_line

main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 500)
main_win.move(300, 150)
main_win.setLayout(main_line)
main_win.show()
app.exec_()

