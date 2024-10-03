import sys
from PyQt5.QtWidgets import *

class MarketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    

    def initUI(self):
        self.f_labels = []
        self.price_details = []
        self.setWindowTitle('Market App')
        self.setGeometry(500, 500, 600, 200)
        fruits = ['apple', 'orange', 'mango', 'strawberry']
        # create dropdown menu for fruits
        fruit_menu = QComboBox(self)
        fruit_menu.addItems(fruits)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MarketApp()
    sys.exit(app.exec_())
