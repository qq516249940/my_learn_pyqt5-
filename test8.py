import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class QLineEditValiddator(QWidget):
    """2. 校验器
比如只能限制输入整数或满足一定条件的字符串"""
    def __init__(self):
        super(QLineEditValiddator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('学习 校验器')

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        DoubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('校检整数类型', intLineEdit)
        formLayout.addRow('校检浮点类型', DoubleLineEdit)
        formLayout.addRow('校检数字和字母类型', validatorLineEdit)

        intLineEdit.setPlaceholderText('整形 例子 1~99')
        DoubleLineEdit.setPlaceholderText('浮点型 -360.00~360.99')
        validatorLineEdit.setPlaceholderText('字母和数字')

        # 整数校验器
        # 创建一个校验器
        intValidator = QIntValidator(self)
        # 设置范围
        intValidator.setRange(1, 99)

        # 浮点校验器
        # 创建一个校验器
        doubleValidator = QDoubleValidator(self)
        # 设置范围
        doubleValidator.setRange(-360, 360)
        # 设置精度
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 字符和数字校验器
        reg = QRegExp('[a-zA-Z0-9]+$')
        # 创建一个校验器
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器
        intLineEdit.setValidator(intValidator)
        DoubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValiddator()
    main.show()
    sys.exit(app.exec_())
