# -*- coding: utf-8 -*
import sys
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton, \
    QInputDialog, QColorDialog, QFontDialog, QFileDialog, QLabel


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.WIDTH = 600
        self.HEIGHT = 300
        self.setGeometry(1920//2 - self.WIDTH // 2, 1080//2 - self.HEIGHT // 2, self.WIDTH, self.HEIGHT)
        self.setFixedSize(self.WIDTH, self.HEIGHT)
        self.setWindowTitle("DialogLerning")
        self.create_button_for_test_dialog()
        self.create_label_for_file_text()

    def create_label_for_file_text(self):
        self.lbl = QLabel(self)
        self.lbl.setWordWrap(True) # автоматический перенос строки
        self.lbl.setFont(QFont("Comic Sans MS", 18))
        self.lbl.setFixedSize(590, 250)
        self.lbl.move(0, 50)

    def create_button_for_test_dialog(self):
        # input
        self.btn_input = QPushButton(self)
        self.btn_input.setText("Test InputDialog")
        self.btn_input.setFont(QFont("Comic Sans MS", 18))
        self.btn_input.setFixedSize(200, 50)
        self.btn_input.clicked.connect(self.showInputDialog)

        # color
        self.btn_color = QPushButton(self)
        self.btn_color.setText("Цвет")
        self.btn_color.setFont(QFont("Comic Sans MS", 18))
        self.btn_color.setFixedSize(200, 50)
        self.btn_color.move(0, 0)
        self.btn_color.clicked.connect(self.showColorDialog)

        # font
        self.btn_font = QPushButton(self)
        self.btn_font.setText("Шрифт")
        self.btn_font.setFont(QFont("Comic Sans MS", 18))
        self.btn_font.setFixedSize(200, 50)
        self.btn_font.move(200, 0)
        self.btn_font.clicked.connect(self.showFontDialog)

        # file
        self.btn_file = QPushButton(self)
        self.btn_file.setText("Файл")
        self.btn_file.setFont(QFont("Comic Sans MS", 18))
        self.btn_file.setFixedSize(200, 50)
        self.btn_file.move(400, 0)
        self.btn_file.clicked.connect(self.showFileDialog)

    def showInputDialog(self):
        text, status = QInputDialog.getText(self, "Input Dialog", "Enter text: ") # окно для ввода текста
        # status -> True, когда игрок нажал на OK | status -> False, если игрок нажал на Cancel и текст не запоминается в переменнную
        if status:
            print("Text:", text, "Status:", status)

    def showColorDialog(self):
        color = QColorDialog.getColor()  # окно для выбора цвета
        if color.isValid():  # если цвет выбран верно - возвращает True
            print("Color:", color.name())
            self.lbl.setStyleSheet(f"color: {color.name()};")  # установили кнопке задний фон


    def showFontDialog(self):
        pass

    def showFileDialog(self):
        pass

def start_app():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_app()

