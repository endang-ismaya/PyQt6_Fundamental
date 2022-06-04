import PyQt6


from PyQt6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

app = QApplication(sys.argv)

# create a Qt Widget, which will be our window
window = QWidget()
window.show()  # Windows are hidden by default

# Start the event loop
app.exec()
