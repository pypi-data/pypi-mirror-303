from PySide6.QtWidgets import QWidget, QListView, QVBoxLayout, QHBoxLayout, QPushButton
from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QIcon

from .process_manager import ProcessManagerWidget
from .py_process_widget.py_process_controller import PyProcessController
from .configure_process import ConfigureProcess
import yaml
import os

BUTTONS = """
QPushButton {
font-size: 10pt;
font-weight: bold; 
color: rgb(215,215,215);
background-color: rgb(25,25,25); 
border-style: outset;
border-radius: 10px;
border-color: rgb(60,60,60); 
border-width: 2px;
padding: 12px;}

QPushButton::hover {background-color: rgb(55,55,55)}

QPushButton:pressed {
background-color: rgb(155,155,155); 
border: 1px solid rgb(155,155,155);}
"""

class ProcessList(QAbstractListModel):
    def __init__(self, process_list:list[PyProcessController]=[]):
        super().__init__()

        self.process_list:list[PyProcessController] = process_list

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and index.isValid():
            return self.process_list[index.row()].dashboard.name_label.text()
        return None

    def rowCount(self, parent=QModelIndex()):
        return len(self.process_list)
    
    def remove_item(self, index):
        self.beginRemoveRows(QModelIndex(), index, index)
        del self.process_list[index]
        self.endRemoveRows()
    
    def add_item(self, py_process:PyProcessController):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.process_list.append(py_process)
        self.endInsertRows()

    def insert_item(self, index, py_process:PyProcessController):
        self.process_list[index] = py_process
        self.dataChanged.emit(index, index)


class ConfigurationWidget(QWidget):
    def __init__(self, config_path:str, process_manager:ProcessManagerWidget=[]):
        super().__init__()

        self.setWindowTitle("Configuration Widget")
        self.setFixedHeight(230)
        self.setFixedWidth(420)
        self.setStyleSheet(BUTTONS)
        self.setWindowIcon(QIcon("icon.PNG"))

        self.config_path:str = config_path

        self.add_process_widget = ConfigureProcess()
        self.add_process_widget.create_process_ready.connect(self.add_to_list)

        self.process_manager = process_manager

        self.list_model = ProcessList(self.process_manager.process_list)
        self.list_view = QListView()
        self.list_view.setModel(self.list_model)

        self.add_process_btn = QPushButton("Add Process")
        self.add_process_btn.clicked.connect(self.add_process)
        self.remove_process_btn = QPushButton("Remove Process")
        self.remove_process_btn.clicked.connect(self.remove_process)
        self.edit_process_btn = QPushButton("Edit Process")
        self.edit_process_btn.clicked.connect(self.edit_process)
        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self.confirm_config)

        btn_layout = QVBoxLayout()
        btn_group = QWidget()
        btn_layout.addWidget(self.add_process_btn)
        btn_layout.addWidget(self.remove_process_btn)
        btn_layout.addWidget(self.edit_process_btn)
        btn_layout.addWidget(self.confirm_btn)
        btn_group.setLayout(btn_layout)



        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_view)
        main_layout.addWidget(btn_group)
        self.setLayout(main_layout)

    def update_list_model(self):
        self.list_model = ProcessList(self.process_manager.process_list)

    def add_process(self):
        self.add_process_widget.show()

    def add_to_list(self):
        self.list_model.add_item(PyProcessController(self.add_process_widget.run_data))

    def remove_process(self):
        selection = self.list_view.selectedIndexes()
        if selection:
            self.list_model.remove_item(selection[0].row())

    def insert_into_list(self):
        self.list_model.insert_item(self.edit_index, PyProcessController(self.edit_config.run_data))
        self.edit_config.close()

    def edit_process(self):
        selection = self.list_view.selectedIndexes()
        if selection:
            self.edit_index = selection[0].row()
            process:PyProcessController = self.list_model.process_list[self.edit_index]
            self.edit_config = ConfigureProcess(process.p_info)
            self.edit_config.create_process_ready.connect(self.insert_into_list)
            self.edit_config.show()

    def confirm_config(self):
        self.update_yaml()
        self.process_manager.process_list = self.list_model.process_list
        self.process_manager.update_layout()


    def update_yaml(self):
        config = []
        for i in self.list_model.process_list:
            config.append(i.p_info.__dict__)
        with open(self.config_path, "w") as f:
            yaml.dump(config, f)


