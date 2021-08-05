import sys   # 系统模块，获得命令行参数
from PyQt5.QtWidgets import QApplication, QWidget, QLabel  # 导入QAppliaction，QLabel以及QWidget

if __name__ == '__main__':
    # 创建一个QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口尺寸，长宽
    w.resize(300,150)
    # 移动窗口(显示时在哪)
    w.move(300,300)
    # 设置窗口标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    # 添加子控件
    label = QLabel(w)
    # 添加文本
    label.setText('hello world')
    # 移动文本(显示时在哪)
    label.move(100, 100)
    # 显示窗口
    w.show()

    # 进入程序主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())
    # sys.exit(app.exec_())
