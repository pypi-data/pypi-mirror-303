# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description:
# @Time   : 2024-08-16 17:05
# @Author : 毛鹏
from mango_ui.init import *


class MangoPushButton(QPushButton):
    def __init__(
            self,
            text,
            theme=THEME,
            parent=None,
            **kwargs
    ):
        super().__init__()
        self.setText(text)
        self.theme = theme
        self.kwargs = kwargs
        if parent:
            self.setParent(parent)

        self.set_stylesheet()
        self.setCursor(Qt.PointingHandCursor)

    def set_stylesheet(self, height=35, width=60):
        style = f'''
        QPushButton {{
            border: 1px solid {self.theme.dark_four};
            color: {self.theme.text_foreground};
            border-radius: {self.theme.radius};	
            background-color: {self.kwargs.get('color') if self.kwargs.get('color') else self.theme.dark_one};
        }}
        QPushButton:hover {{
            background-color: {self.theme.dark_three};
        }}
        QPushButton:pressed {{	
            background-color: {self.theme.dark_four};
        }}
        '''
        self.setStyleSheet(style)
        self.setMinimumHeight(height)
        self.setMinimumWidth(width)
