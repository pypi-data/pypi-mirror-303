# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-10-14 21:13
# @Author : 毛鹏
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea, QWidget, QVBoxLayout

from mango_ui.settings.settings import THEME


class MangoScrollArea(QScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.setWidget(self.scroll_widget)
        self.layout = QVBoxLayout(self.scroll_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_widget.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignTop)

        # self.setStyleSheet(f"background-color: {THEME.white}")
        self.setStyleSheet(f"""
                QScrollArea {{
            background-color: {THEME.dark_three};
            padding: 5px;
            border-radius: {THEME.radius}px;
            border: 1px solid {THEME.bg_three};
        }}
        
        QScrollBar:horizontal {{
            border: none;
            background: {THEME.bg_one};
            height: 8px;
            margin: 0px 21px;
            border-radius: 0px;
        }}
        
        QScrollBar::handle:horizontal {{
            background: {THEME.context_hover};
            min-width: 25px;
            border-radius: 4px;
        }}
        
        QScrollBar::add-line:horizontal {{
            border: none;
            background: {THEME.dark_four};
            width: 20px;
            border-top-right-radius: 4px;
            border-bottom-right-radius: 4px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }}
        
        QScrollBar::sub-line:horizontal {{
            border: none;
            background: {THEME.dark_four};
            width: 20px;
            border-top-left-radius: 4px;
            border-bottom-left-radius: 4px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }}
        
        QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {{
            background: none;
        }}
        
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
            background: none;
        }}
        
        QScrollBar:vertical {{
            border: none;
            background: {THEME.bg_one};
            width: 8px;
            margin: 21px 0;
            border-radius: 0px;
        }}
        
        QScrollBar::handle:vertical {{
            background: {THEME.context_hover};
            min-height: 25px;
            border-radius: 4px;
        }}
        
        QScrollBar::add-line:vertical {{
            border: none;
            background: {THEME.dark_four};
            height: 20px;
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }}
        
        QScrollBar::sub-line:vertical {{
            border: none;
            background: {THEME.dark_four};
            height: 20px;
            border-top-left-radius: 4px;
            border-top-right-radius: 4px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }}

        """)
