# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-10-16 15:46
# @Author : 毛鹏
class WidgetTool:

    @staticmethod
    def remove_layout(layout):
        while layout.count() > 0:
            widget = layout.itemAt(0).widget()
            if widget is not None:
                layout.removeWidget(widget)
                widget.deleteLater()
