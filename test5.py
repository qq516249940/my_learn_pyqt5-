import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton

def onClick_Button():
    print('1、QWidget,窗口')
    print("widget.x()= %d" % widget.x())    # 窗口横坐标
    print("widget.y()= %d" % widget.y())    # 窗口纵坐标
    print("widget.width()= %d" % widget.width())    # 工作区宽度
    print("widget.height()= %d" % widget.height())    # 工作区高度

    print('------------------------------------------')

    print('2、gemetry，工作区')
    print("widget.geometry().x()= %d" % widget.geometry().x())    # 工作区横坐标
    print("widget.geometry().y()= %d" % widget.geometry().y())    # 工作区纵坐标
    print("widget.geometry().width()= %d" % widget.geometry().width())    # 工作区宽度
    print("widget.geometry().height()= %d" % widget.geometry().height())    # 工作区宽度

    print('------------------------------------------')

    print('3、frameGeometry，工作区+标题栏')
    print("widget.frameGeometry().x()= %d" % widget.frameGeometry().x())    # 窗口横坐标
    print("widget.frameGeometry().y()= %d" % widget.frameGeometry().y())    # 窗口纵坐标
    print("widget.frameGeometry().width()= %d" % widget.frameGeometry().width())    # 窗口宽度
    print("widget.frameGeometry().height()= %d" % widget.frameGeometry().height())    # 窗口高度

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24, 52)

widget.resize(300, 244)
widget.move(250, 200)

widget.setWindowTitle('QWidget')

widget.show()

sys.exit(app.exec_())



