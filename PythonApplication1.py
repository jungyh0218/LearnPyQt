
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'Hello PyQt5'
        self.left = 20
        self.top = 20
        self.width = 1080
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        button = QPushButton("Push this Button", self)
        button.setToolTip("Example button")
        button.move(50, 70)
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())