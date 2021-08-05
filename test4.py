import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class QMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWin, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

        # 设置状态栏
        self.status = self.statusBar()
        self.status.showMessage('这是状态栏，消息只存在五秒', 5000)

        # 设置按钮
        self.button1 = QPushButton('关闭主窗口')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        MainFrame = QWidget()
        MainFrame.setLayout(layout)
        self.setCentralWidget(MainFrame)

    # 主窗口居中显示
    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLeft, newTop)

    # 按钮单击事件的方法(自定义的槽)
    def onButtonClick(self):
        # sender是发送信号的对象
        sander = self.sender()
        print(sander.text() + '按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('about_us_bk.jpg'))
    main = QMainWin()
    main.show()
    sys.exit(app.exec_())
