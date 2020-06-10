from sys import argv, exit

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("test_dialog.ui", self)
        self.num1, self.num2, self.symbol, self.text = '', '', '', ''

    @pyqtSlot()
    def push_button(self):  # 9
        if self.symbol == '':
            self.num1 += '9'
        else:
            self.num2 += '9'
        self.text += '9'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_2(self):  # 4
        if self.symbol == '':
            self.num1 += '4'
        else:
            self.num2 += '4'
        self.text += '4'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_3(self):  # 1
        if self.symbol == '':
            self.num1 += '1'
        else:
            self.num2 += '1'
        self.text += '1'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_4(self):  # 8
        if self.symbol == '':
            self.num1 += '8'
        else:
            self.num2 += '8'
        self.text += '8'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_5(self):  # 5
        if self.symbol == '':
            self.num1 += '5'
        else:
            self.num2 += '5'
        self.text += '5'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_6(self):  # 2
        if self.symbol == '':
            self.num1 += '2'
        else:
            self.num2 += '2'
        self.text += '2'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_7(self):  # =
        num1, num2 = int(self.num1), int(self.num2)
        self.num1, self.num2 = '', ''
        if self.symbol == '+':
            self.text == str(num1 + num2)
        elif self.symbol == '-':
            self.text == str(num1 - num2)
        elif self.symbol == '*':
            self.text == str(num1 * num2)
        else:
            self.text == str(num1 / num2)
        self.symbol == ''
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_8(self):  # 3
        if self.symbol == '':
            self.num1 += '3'
        else:
            self.num2 += '3'
        self.text += '3'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_9(self):  # 6
        if self.symbol == '':
            self.num1 += '6'
        else:
            self.num2 += '6'
        self.text += '6'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_10(self):  # 7
        if self.symbol == '':
            self.num1 += '7'
        else:
            self.num2 += '7'
        self.text += '7'
        QLineEdit.text_box().displayText(self) == self.text

    @pyqtSlot()
    def push_button_11(self):  # 0
        if self.symbol == '':
            self.num1 += '0'
        else:
            self.num2 += '0'
        self.text += '0'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_12(self):  # Del
        self.text, self.num1, self.num2, self.symbol = '', '', '', ''
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_13(self):  # +
        if self.symbol != '':
            a = MainWindow()
            a.push_button_7()
        self.symbol == '+'
        self.text += '+'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_14(self):  # -
        if self.symbol != '':
            pass
        else:
            self.symbol == '-'
            self.text += '-'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_15(self):  # *
        if self.symbol != '':
            pass
        else:
            self.symbol == '*'
            self.text += '×'
        QLineEdit.lineEdit.displayText(self) == self.text

    @pyqtSlot()
    def push_button_16(self):  # /
        if self.symbol != '':
            pass
        else:
            self.symbol == '/'
            self.text += '÷'
        QLineEdit.text_box.displayText(self) == self.text

    @pyqtSlot()
    def text_box(self):
        pass


if __name__ == '__main__':
    app = QApplication(argv)
    qui = MainWindow()
    qui.show()
    exit(app.exec_())
