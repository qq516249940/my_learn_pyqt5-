from PyQt5.Qt import *    # 别问为什么这么写，问就是懒，这样做的好处是可以不管什么包都导入，不需要一点点导包，缺点就是占点内存
import sys    

# sys是什么
# 我们的代码，到时候的执行方式，1、右击run去执行，2、命令行Python代码名称

# argv:当别人通过命令行启动这个程序的时候，可以设定一种功能(接收命令行传递的参数来执行不同的业务逻辑)
args = sys.argv
print(args)
if args[1] == '1':
	print("hello world")
else:
	print("hello pyqt")


app = QApplication(sys.argv)
# 当有很多个文件的时候，想要获取入口文件参数时
print(app.arguments())
print(qApp.arguments())   # qApp是全局变量


# 创建控件，设置控件(大小，位置，样式)，事件，信号的处理

# 1、创建控件
# 控件创建好后(没有父控件)，则把它当作顶层控件(窗口)，系统会自动的给窗口添加一些装饰(标题栏)，窗口控件具备一些性质(设置标题，图标)
window = QWidget()

# 2、设置控件
window.setWindowTitle("程序基本结构分析") # 设置窗口标题
window.resize(300,150) # 设置窗口尺寸，长宽
window.move(300,300)  # 移动窗口(显示时在哪),长高

# 控件也可以作为一个容器承载其他控件
label = QLabel(window)
label.setText('hello world')
label.move(50,50)

# 3、展示控件
# 刚创建好一个控件后(没父控件)，需要手动展示
window.show()

# exit(退出码)，正常退出是0，程序内部错误是其他的错误码，通过传递不同的错误码，可以知道怎么退出的。
sys.exit(app.exec())
