# Import PyQt5 classes
import sys
import re
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication

from calculator import *


class MathConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MathConsumer, self).__init__(parent)
        self.setupUi(self)

        self.btnCalculate.clicked.connect(self.performOperation)

    def performOperation(self):
        num1 = self.edtNumber1.text()
        num2 = self.edtNumber2.text()
        if len(num1) and len(num2) and len(num1) == len(re.findall(r'[0-9-]', num1)) and len(num2) == len(re.findall(r'[0-9-]', num2)):
            status = True
            for val in [num1, num2]:
                count = 0
                for index, char in enumerate(val):
                    if char == '.':
                        count += 1
                    if index and char == '-':
                        self.edtResult.setText('E')
                        status = False
                if count > 1 or (count == 1 and len(val) == 1):
                    status = False
                    self.edtResult.setText('E')
            if status:
                num1 = int(num1)
                num2 = int(num2)
                op = self.cboOperation.currentText()
                if op == '+':
                    self.edtResult.setText(str(num1 + num2))
                elif op == '-':
                    self.edtResult.setText(str(num1 - num2))
                elif op == '*':
                    self.edtResult.setText(str(num1 * num2))
                elif op == '/':
                    self.edtResult.setText(str(num1 / num2))
        elif len(num1) and len(num2) and len(num1) == len(re.findall(r'[0-9.-]', num1)) and len(num2) == len(re.findall(r'[0-9.-]', num2)):
            status = True
            for val in [num1, num2]:
                count = 0
                for index, char in enumerate(val):
                    if char == '.':
                        count += 1
                    if index and char == '-':
                        self.edtResult.setText('E')
                        status = False
                if count > 1 or (count == 1 and len(val) == 1):
                    status = False
                    self.edtResult.setText('E')
            if status:
                num1 = float(num1)
                num2 = float(num2)
                op = self.cboOperation.currentText()
                if op == '+':
                    self.edtResult.setText(str(num1 + num2))
                elif op == '-':
                    self.edtResult.setText(str(num1 - num2))
                elif op == '*':
                    self.edtResult.setText(str(num1 * num2))
                elif op == '/':
                    self.edtResult.setText(str(num1 / num2))
        else:
            self.edtResult.setText('E')


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MathConsumer()

    currentForm.show()
    sys.exit(currentApp.exec_())

