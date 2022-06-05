import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# create a class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Windows Title
        self.setWindowTitle("PyQt6 Class Window")

        # Variables
        self.button_is_checked = True

        # create a button | signal & slots
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        # set window fixed sized
        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(400, 300))

        # set the central widget of the window
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print(f"Released Checked? {self.button_is_checked}")

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)

        # also change the window title
        self.setWindowTitle("Button Was Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(f"Checked? {self.button_is_checked}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
