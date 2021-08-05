# importing the required libraries
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys
  
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # set the title
        self.setWindowTitle("Move")
  
        # setting  the geometry of window
        self.setGeometry(0, 0, 400, 400)
  
        # creating a label widget
        self.widget = QLabel('Moved', self)
  
        # moving the widget
        # move(left, top)
        self.widget.move(50, 50)
  
  
        # show all the widgets
        self.show()
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())