# making a button with pyqt5

from PyQt5 import QtWidgets 




from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import datetime

class JoseClass(QMainWindow):
    def __init__(self):
        super(JoseClass, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Jose next project of making desktop software")
        self.hello()

    def umair(self):
        print("umair clicked me")
        print (datetime.datetime.now())
        # print(datetime.now())

    def jose(self):
        print("jose clicked me")

    def hello(self):    
        self.button = QtWidgets.QPushButton("jose click me", self)
        self.button.move(50, 50)
        self.button.clicked.connect(self.jose)  

        self.button2 = QtWidgets.QPushButton("umair click me", self)
        self.button2.move(50, 100)
        self.button2.clicked.connect(self.umair)


        self.show()
        
    


# make a q applcation

app = QApplication(sys.argv)
window = JoseClass()
sys.exit(app.exec_())
