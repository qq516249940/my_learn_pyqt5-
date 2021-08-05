import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPalette,QPixmap

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>点击领取3.8折咖啡券</font>")
        # 填充整个屏幕
        label1.setAutoFillBackground(True)
        patette = QPalette()
        # 调色板，设置背景色
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(patette)
        # 设置文本对齐方式
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("about_us_bk.jpg"))

        # 如果设为True，用浏览器打开，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText('<a href=https://www.baidu.com>面向百度编程</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')
    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
