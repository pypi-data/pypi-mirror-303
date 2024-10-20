from PySide6.QtWidgets import (QWidget, QGridLayout, QScrollArea)
from PySide6.QtCore import Qt
from .py_process_widget.py_process_controller import PyProcessController


class ProcessManagerWidget(QScrollArea):
    def __init__(self, process_list:list[PyProcessController]=[]):
        super().__init__()

        self.process_list = process_list
        self.update_layout()

    def update_layout(self):
        self.content = QWidget()
        self.l = QGridLayout()
        ROW = 0
        COL = 0
        for i in range(len(self.process_list)):
            if i % 4 == 0:
                ROW += 1
                COL = 0
                self.l.addWidget(self.process_list[i], ROW, COL, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
            else:
                COL += 1
                self.l.addWidget(self.process_list[i], ROW, COL, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.content.setLayout(self.l)

        self.setWidget(self.content)
        self.setWidgetResizable(True)
        self.update()


