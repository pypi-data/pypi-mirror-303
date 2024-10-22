import asyncio

import sys
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class AsyncWorker(QObject):
    finished = Signal(str)  # 修改为带有返回值的完成信号
    progress = Signal(str)  # 定义进度信号

    async def do_async_work(self):
        result = ""
        for i in range(100):
            self.progress.emit(f"Progress: {i + 1} seconds")  # 发出进度信号
            result += f"{i + 1} "  # 收集结果
        self.finished.emit(result.strip())  # 发出完成信号并传递结果


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.start_button = QPushButton("Start Async Work")
        self.progress_label = QLabel("Progress: 0 seconds")
        self.result_label = QLabel("Result: ")
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.progress_label)
        self.layout.addWidget(self.result_label)  # 添加结果标签
        self.setLayout(self.layout)

        self.worker = AsyncWorker()
        self.worker.progress.connect(self.update_progress)  # 连接进度信号
        self.worker.finished.connect(self.async_task_finished)  # 连接完成信号

        self.start_button.clicked.connect(self.start_async_task)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.loop.run_until_complete(asyncio.sleep(0)))
        self.loop = asyncio.new_event_loop()

    def start_async_task(self):
        self.timer.start(100)  # 启动定时器
        asyncio.run_coroutine_threadsafe(self.worker.do_async_work(), self.loop)

    def update_progress(self, message):
        self.progress_label.setText(message)  # 更新进度标签

    def async_task_finished(self, result):
        print("Async task finished.")
        self.timer.stop()  # 停止定时器
        self.result_label.setText(f"Result: {result}")  # 显示结果


# 创建 QApplication 实例
app = QApplication(sys.argv)

widget = MyWidget()
widget.show()

# 启动事件循环
app.exec()
