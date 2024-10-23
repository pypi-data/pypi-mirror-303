import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from mango_ui import *



class CronGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cron 表达式生成器")
        self.setGeometry(100, 100, 300, 200)

        # 创建布局
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout_2 = QHBoxLayout()

        layout.addLayout(h_layout)
        layout.addLayout(h_layout_2)
        # 创建周几复选框
        self.weekday_checkboxes = []
        weekdays = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]
        h_layout.addWidget(MangoLabel("选择周几 (可多选):"))

        for day in weekdays:
            checkbox = MangoCheckBox(day)
            self.weekday_checkboxes.append(checkbox)
            h_layout.addWidget(checkbox)

        # 创建时间选择器
        self.time_edit = MangoTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")  # 设置显示格式为 HH:mm
        h_layout_2.addWidget(MangoLabel("选择时间 (HH:MM):"))
        h_layout_2.addWidget(self.time_edit)

        # 创建提交按钮
        self.submit_button = MangoPushButton("提交")
        self.submit_button.clicked.connect(self.generate_cron)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def generate_cron(self):
        selected_days = []
        for checkbox in self.weekday_checkboxes:
            if checkbox.isChecked():
                selected_days.append(str(self.weekday_checkboxes.index(checkbox)))

        time = self.time_edit.time()
        hour = time.hour()
        minute = time.minute()
        cron_expression = f"{minute} {hour} * * {','.join(selected_days)}"
        print(cron_expression)
        return cron_expression


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CronGenerator()
    window.show()
    sys.exit(app.exec())
