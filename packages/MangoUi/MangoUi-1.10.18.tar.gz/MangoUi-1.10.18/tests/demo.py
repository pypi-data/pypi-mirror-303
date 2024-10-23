import sys
import matplotlib
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 设置字体为支持中文的字体
matplotlib.rcParams['font.family'] = 'SimHei'  # 或者 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False  # 显示负号


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("近3个月趋势图")
        self.setGeometry(100, 100, 800, 600)

        # 创建图表类实例
        self.trend_plot = LinePlot()
        api_count = [{'name': 'API', 'value': [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]},
                     {'name': 'UI', 'value': [12, 4, 13, 0, 1, 0, 0, 0, 0, 0, 0, 0]}]
        self.trend_plot.draw(api_count)

        # 设置主窗口的中心部件
        self.setCentralWidget(self.trend_plot)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("饼状图示例")
        self.setGeometry(100, 100, 800, 600)

        # 主布局
        main_layout = QVBoxLayout()

        # 创建 Matplotlib 画布
        self.canvas = PiePlot()
        main_layout.addWidget(self.canvas)

        # 数据对象
        data = [
            {"value": 51, "name": "前端"},
            {"value": 48, "name": "接口"}
        ]

        # 绘制饼状图
        self.canvas.draw(data)

        # 设置主窗口的中心部件
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
