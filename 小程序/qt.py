# encoding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QInputDialog, QLabel, QGridLayout

#class Example
class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.InitUI()
 
    def InitUI(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("Input Dialog")

        #按钮
        self.btn = QPushButton("Dialog", self)
        self.btn.setToolTip('This is a <b>button</b> for test')
        #self.btn.move(20, 20)
        layout.addWidget(self.btn, 0, 0)
        self.btn.clicked.connect(self.ShowDialog)
 
        #文本框
        self.le = QLineEdit(self)
        #self.le.move(100, 20)
        layout.addWidget(self.le, 1, 0)

        #文本
        self.te = QLabel('test')
        message = self.te.text()
        #self.te.move(20, 100)
        layout.addWidget(self.te, 2, 0)


 
        self.show()
 
    def ShowDialog(self):
        text,ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.te.setText(str(text))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())