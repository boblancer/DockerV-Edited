import os
import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ClickableLabelWidget import ClickableLabel

from pyside_material import apply_stylesheet


class DashboardItem(QWidget):
    def __init__(self, amount: int, image_path: str, name: str):
        QWidget.__init__(self, None)

        self.picture = QLabel()
        self.picture.setPixmap(QPixmap(image_path))

        self.icon = ClickableLabel(self.picture)
        self.amount = ClickableLabel(str(amount))
        self.name = ClickableLabel(name)

        self.amount.setStyleSheet('font-size: 30pt; font-weight: Bold;')
        self.name.setStyleSheet('font-size: 20pt;')

        self.picture.setFixedSize(100, 100)
        self.picture.setScaledContents(True)

        layout = QHBoxLayout(self)
        layout.setSpacing(100)
        layout.addWidget(self.picture)
        layout.addWidget(self.amount)
        layout.addWidget(self.name)

        layout.setAlignment(Qt.AlignLeft)

        self.setLayout(layout)

    def getClickableLabel(self):
        return [self.amount, self.name]

