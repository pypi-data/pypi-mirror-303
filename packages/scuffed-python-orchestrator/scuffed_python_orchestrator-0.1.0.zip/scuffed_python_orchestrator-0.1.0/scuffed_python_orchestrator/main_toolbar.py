from PySide6.QtWidgets import QMainWindow, QToolBar, QWidget, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon

from .configure_process import ConfigureProcess
from .process_manager import ProcessManagerWidget
from .py_process_widget.py_process_controller import PyProcessController
from .py_process_widget.process_info import ProcessInfo
from .config_widget import ConfigurationWidget

import yaml

TOOL_BUTTON = """
QToolButton {
    padding: 15px;
    text-align: left;
    font-size: 14px;
}
QToolButton:hover {
    background-color: #4a4a4a;
}
QToolButton:pressed {
    background-color: #5a5a5a;
}

QToolButton#exit_button {
    padding: 25px 45px;
}
QToolButton#exit_button:hover {
    padding: 25px 45px;
}
"""

class SpacerWidget(QWidget):
    def __init__(self, width=30):
        super().__init__()
        self.setFixedWidth(width)
        self.setFixedHeight(width)


class MainToolBar(QToolBar):
    def __init__(self, main_window:QMainWindow, main_widget:ProcessManagerWidget, config_path:str):
        super().__init__()

        self.main_widget:ProcessManagerWidget = main_widget
        self.config_path = config_path
        self.config_widget = ConfigurationWidget(self.config_path, self.main_widget)

        self.setAllowedAreas(Qt.LeftToolBarArea | Qt.RightToolBarArea)

        self.start_orch_btn = QAction(QIcon(), "Start\nOrchestrator")
        self.start_orch_btn.triggered.connect(self.start_orch)
        self.stop_orch_btn = QAction(QIcon(), "Stop\nOrchestrator")
        self.stop_orch_btn.setEnabled(False)
        self.stop_orch_btn.triggered.connect(self.stop_orch)

        self.set_configuration_btn = QAction(QIcon(), "Set Current\nConfiguration")
        self.set_configuration_btn.triggered.connect(self.set_configuration)

        self.import_config_btn = QAction(QIcon(), "Import\nConfiguration")
        self.import_config_btn.triggered.connect(self.import_config)

        self.export_config_btn = QAction(QIcon(), "Export\nConfiguration")
        self.export_config_btn.triggered.connect(self.export_configuration)

        self.exit_btn = QAction(QIcon(), "Exit")
        self.exit_btn.triggered.connect(main_window.close)

        self.addWidget(SpacerWidget())
        self.addSeparator()
        self.addAction(self.start_orch_btn)
        self.addAction(self.stop_orch_btn)
        self.addSeparator()

        self.addWidget(SpacerWidget())
        self.addSeparator()
        self.addAction(self.set_configuration_btn)
        self.addAction(self.import_config_btn)
        self.addAction(self.export_config_btn)
        self.addSeparator()

        self.addWidget(SpacerWidget())
        self.addSeparator()
        self.addAction(self.exit_btn)
        self.addSeparator()

        self.widgetForAction(self.exit_btn).setObjectName("exit_button")
        self.setStyleSheet(TOOL_BUTTON)

    def start_orch(self):
        self.start_orch_btn.setEnabled(False)
        self.set_configuration_btn.setEnabled(False)
        self.config_widget.close()
        for i in self.main_widget.process_list:
            i.start_worker()
        self.stop_orch_btn.setEnabled(True)
        
    def stop_orch(self):
        self.stop_orch_btn.setEnabled(False)
        self.set_configuration_btn.setEnabled(True)
        for i in self.main_widget.process_list:
            i.stop_worker()
            i.kill_process()
        self.start_orch_btn.setEnabled(True)
        
    def import_config(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Orchestrator .yaml", "", "*.yaml")
        if file_path:
            with open(file_path, "r") as f:
                config = yaml.safe_load(f)
            
            process_list = []
            for i in config:
                process_list.append(PyProcessController(ProcessInfo(i['name'], i['run_file'], i['interpreter'], i['sched'], i['has_progress'], i['sched_data'])))
            
            self.main_widget.process_list = process_list
            self.config_widget = ConfigurationWidget(self.config_path, self.main_widget)
            self.main_widget.update_layout()

    def set_configuration(self):
        self.config_widget.show()

    def export_configuration(self):
        filepath = QFileDialog.getExistingDirectory(self, "Select Save Location", "")
        config = []
        for i in self.main_widget.process_list:
            config.append(i.p_info.__dict__)
        with open(f"{filepath}\\config.yaml", "w") as f:
            yaml.dump(config, f)

    


