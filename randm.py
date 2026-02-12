import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QRect
import random



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # ===== Main window setup (from <widget class="QMainWindow">) =====
        self.setObjectName("MainWindow")
        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 400, 600)


        # ===== Central widget =====
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)


        # Common font from your UI
        corsiva_30 = QFont("Monotype Corsiva", 30)


        # ===== QLabel: name="text" =====
        self.text = QLabel(self.centralwidget)
        self.text.setObjectName("text")
        self.text.setGeometry(QRect(70, 50, 281, 51))
        self.text.setFont(corsiva_30)
        self.text.setText("Random Generator")


        # ===== QLabel: name="label_2" =====
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(120, 200, 161, 41))
        self.label_2.setFont(corsiva_30)
        self.label_2.setText("TextLabel")


        # ===== QPushButton: name="generate" =====
        self.generate = QPushButton(self.centralwidget)
        self.generate.setObjectName("generate")
        self.generate.setGeometry(QRect(100, 350, 191, 61))
        self.generate.setFont(corsiva_30)
        self.generate.setText("Generate")


        self.generate.clicked.connect(self.on_generate_clicked)

    def on_generate_clicked(self):
        value = random.randint(1, 1000)
        self.label_2.setText(str(value))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
