from PySide6.QtWidgets import (QApplication, QMainWindow, QStyleFactory)
from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtGui import QIcon
import sys
import os
import yaml

from scuffed_orchestrator.process_manager import ProcessManagerWidget
from scuffed_orchestrator.main_toolbar import MainToolBar
from scuffed_orchestrator.py_process_widget.process_info import ProcessInfo
from scuffed_orchestrator.py_process_widget.py_process_controller import PyProcessController

from PySide6.QtCore import QObject, QEvent

class ToolTipFilter(QObject):
    def eventFilter(self, obj, event:QEvent):
        if event.type() == QEvent.ToolTip:
            return True
        return super().eventFilter(obj, event)


basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        config_path = os.path.join(basedir, "config.yaml")
        icon_path = os.path.join(basedir, "icon.PNG")

        self.setWindowTitle("Scuffed Orchestrator")
        self.setWindowIcon(QIcon(icon_path.__str__()))
        self.setFixedHeight(800)
        self.setFixedWidth(1600)

        config=None
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        
        p_list = []
        if config:
            for i in config:
                p_list.append(PyProcessController(ProcessInfo(i['name'], 
                                                              i['run_file'], 
                                                              i['interpreter'], 
                                                              i['sched'], 
                                                              i['has_progress'], 
                                                              i['sched_data'])))

        
        self.main_widget = ProcessManagerWidget(p_list)
        self.toolbar = MainToolBar(self, self.main_widget, config_path)
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        self.setCentralWidget(self.main_widget)

    def closeEvent(self, event):
        for proc in self.main_widget.process_list:
            proc.stop_worker()
            proc.kill_process()
        event.accept()



app = QApplication(sys.argv)
app.setStyle(QStyleFactory.create("Fusion"))

tool_tip_filter = ToolTipFilter()
app.installEventFilter(tool_tip_filter)


# Come back to later
# screen = app.primaryScreen()

# print(screen.size().width(), screen.size().height())


w = MainWindow()
w.show()

app.exec()




# Load Configuration
# The 3 Other configurations
# Yaml load and dump
# Remove add/remove process from toolbar for now




# Process worker could maybe be centralized



# Config builder
# Open new frame which takes over thread?


