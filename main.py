from PyQt5.QtWidgets import QWidget, QApplication
from design import Ui_Form as Design
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        self.plainTextEdit.setPlainText("")
        if self.checkBox.isChecked():
            self.plainTextEdit.appendPlainText("Мак Фреш")
        if self.checkBox_2.isChecked():
            self.plainTextEdit.appendPlainText("Чизбургер")
        if self.checkBox_3.isChecked():
            self.plainTextEdit.appendPlainText("Роял")
        if self.checkBox_4.isChecked():
            self.plainTextEdit.appendPlainText("Соус кари")
        if self.checkBox_5.isChecked():
            self.plainTextEdit.appendPlainText("Чай черный")

app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())