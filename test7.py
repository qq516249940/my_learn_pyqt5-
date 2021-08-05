
import sys
from PyQt5.QtWidgets import *

class QLineEditEchoMode(QWidget):
    """QLineEdit类是一个单行文本控件，可输入单行字符串，可以设置回显模式(Echomode)和掩码模式
1. 回显模式(Echomode)
回显模式就是当键盘被按下后，显示了什么

Normal 正常的回显模式
NoEcho 不回显模式(什么都没出现)
Password 密码
PasswordEchoOnEdit 先是显示，然后过了几秒就不显示
 """
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('学习 文本框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnLineEdit = QLineEdit()

        formLayout.addRow("请我喝一杯咖啡 Normal", normalLineEdit)
        formLayout.addRow("请我喝2杯咖啡 noEcho", noEchoLineEdit)
        formLayout.addRow("请我喝3杯咖啡 password", passwordLineEdit)
        formLayout.addRow("请我喝4杯咖啡 passwordEchoOnEdit", passwordEchoOnLineEdit)

        # placeoldertext  文本输入框内的灰色提示
        normalLineEdit.setPlaceholderText("input Normal")
        noEchoLineEdit.setPlaceholderText("input noEcho")
        passwordLineEdit.setPlaceholderText("input password")
        passwordEchoOnLineEdit.setPlaceholderText("input passwordEchoOnEdit")
# 设置回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
