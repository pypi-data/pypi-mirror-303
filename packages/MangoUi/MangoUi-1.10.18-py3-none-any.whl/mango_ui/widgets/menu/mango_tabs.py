# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-10-14 17:30
# @Author : 毛鹏
from PySide6.QtWidgets import QTabWidget

from mango_ui.settings.settings import THEME

class MangoTabs(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f"""
            QTabWidget {{
                background-color: {THEME.dark_three}; /* 设置整个选项卡的底色 */
            }}
            QTabBar::tab {{
                border: none;  /* 去掉选项卡的边框 */
                padding: 10px; /* 内边距 */
            }}
            QTabBar::tab:selected {{
                background: {THEME.bg_three}; /* 选中时的背景颜色 */
            }}
            QTabBar::tab:hover {{
                background: {THEME.dark_three}; /* 鼠标悬停时的背景颜色 */
            }}
            QTabBar::tab {{                                
                border-right: 1px solid {THEME.dark_four}; /* 保留按钮之间的边框 */
            }}
            QTabBar::tab:last {{
                border-right: none; /* 最后一个选项卡不显示右边框 */
            }}
            QTabWidget::pane {{
                border: 1px solid {THEME.dark_four}; /* 底部横条 */
                border-left: none; /* 取消顶部边框 */
                border-right: none; /* 取消顶部边框 */
                border-bottom: none; /* 取消顶部边框 */
            }}
        """)
