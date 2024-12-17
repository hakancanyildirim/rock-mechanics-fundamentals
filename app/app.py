import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock Mechanics Toolkit")

        self.setFixedSize(QSize(int(1920/1.8), int(1080/1.5)))
        
        #button = QPushButton("testing")
        #self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
