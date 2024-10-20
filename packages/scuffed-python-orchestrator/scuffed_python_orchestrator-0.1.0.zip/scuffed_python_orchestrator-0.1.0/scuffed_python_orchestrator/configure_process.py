from PySide6.QtWidgets import (QPushButton, QCheckBox, QWidget, QMessageBox, 
                               QFileDialog, QComboBox, QInputDialog, 
                               QLineEdit, QGridLayout, QHBoxLayout)
from PySide6.QtGui import QIcon, QIntValidator
from PySide6.QtCore import Signal, Qt
from .py_process_widget.process_info import ProcessInfo
import sys
import pathlib


BUTTONS = """
QCheckBox {
font-size: 10pt;
font-weight: bold;
color: rgb(215,215,215);
spacing: 5px;
}
QCheckBox::indicator {
width: 20px;
height: 20px;
}
QCheckBox::indicator:unchecked {
border: 2px solid rgb(60,60,60);
background: rgb(25,25,25);
image: url(none);
}
QCheckBox::indicator:checked {
border: 2px solid rgb(155,155,155);
background: rgb(155,155,155);
image: url(icon.PNG);
}
QCheckBox::indicator:hover {
background: rgb(55,55,55);
}

QPushButton {
color: rgb(215,215,215);
background-color: rgb(25,25,25); 
border-style: outset; 
border-radius: 4px;
border-color: rgb(60,60,60); 
border-width: 1px;
padding: 4px;}

QPushButton::hover {background-color: rgb(55,55,55)}

QPushButton:pressed {
background-color: rgb(155,155,155); 
border: 1px solid rgb(155,155,155);}

QComboBox {
color: rgb(215,215,215);
background-color: rgb(25,25,25); 
border-style: outset; 
border-radius: 4px;
border-color: rgb(60,60,60); 
border-width: 1px;
padding: 4px;}

QComboBox::hover {background-color: rgb(55,55,55)}
"""


SCHEDULE_WIDGET = """
QComboBox:disabled {
color: rgb(130,130,130);
background-color: rgb(45,45,45);
border-color: rgb(80,80,80);}
"""


class ScheduleWidget(QWidget):
    def __init__(self):
        super().__init__() 

        self.value_input = QLineEdit()
        self.value_input.setFixedWidth(50)
        input_valid = QIntValidator(1, 999, self)
        self.value_input.setValidator(input_valid)

        self.time_value_set = QComboBox()
        self.time_value_set.addItems(["Seconds", "Minutes", "Hours", "Days", "Weeks"])
        self.setStyleSheet(SCHEDULE_WIDGET)

        l = QHBoxLayout()
        l.addWidget(self.value_input)
        l.addWidget(self.time_value_set)

        self.setLayout(l)
        


class ConfigureProcess(QWidget):
    create_process_ready = Signal()

    def __init__(self, run_data:ProcessInfo=None):
        super().__init__()

        self.setWindowTitle("Configure Python Process")
        self.setFixedHeight(170)
        self.setFixedWidth(380)
        self.setStyleSheet(BUTTONS)
        self.setWindowIcon(QIcon("icon.PNG"))

        self.run_data:ProcessInfo = run_data

        self.py_file_label = QLineEdit()
        self.py_file_label.setReadOnly(True)
        if self.run_data:
            self.py_file_label.setText(run_data.run_file)
        else:
            self.py_file_label.setPlaceholderText("No File Selected")
        self.set_py_file_btn = QPushButton("Python Run File")
        self.set_py_file_btn.clicked.connect(self.set_py_file)

        self.py_interpreter_label = QLineEdit()
        self.py_interpreter_label.setReadOnly(True)
        if self.run_data:
            self.py_interpreter_label.setText(run_data.interpreter)
        else:
            self.py_interpreter_label.setPlaceholderText("No Interpreter Selected")
        self.set_py_interpreter_btn = QPushButton("Set Python Interpreter")
        self.set_py_interpreter_btn.clicked.connect(self.set_py_interpeter)

        
        self.set_schedule_widget = ScheduleWidget()
        self.set_schedule_widget.setEnabled(False)

        self.set_schedule = QComboBox()
        self.set_schedule.addItem("Run Indefinitely")
        self.set_schedule.addItem("Run Periodically")
        # self.set_schedule.addItem("Defined Schedule")
        if self.run_data:
            if self.run_data.sched == "Run Periodically":
                self.set_schedule.setCurrentText("Run Periodically")
                self.set_schedule_widget.setEnabled(True)
                self.set_schedule_widget.time_value_set.setCurrentText(self.run_data.sched_data["time_unit"])
                self.set_schedule_widget.value_input.setText(self.run_data.sched_data["value"])
        self.set_schedule.textActivated.connect(self.set_schedule_func)

        self.use_progress_bar = QCheckBox("Has Progress Steps?")

        self.create_process_btn = QPushButton("Create Process")
        self.create_process_btn.clicked.connect(self.create_process)


        l = QGridLayout()
        
        l.addWidget(self.set_py_file_btn, 0, 0)
        l.addWidget(self.py_file_label, 0, 1)

        l.addWidget(self.set_py_interpreter_btn, 1, 0)
        l.addWidget(self.py_interpreter_label, 1, 1)

        l.addWidget(self.set_schedule, 2, 0)
        l.addWidget(self.set_schedule_widget, 2, 1)

        l.addWidget(self.create_process_btn, 3, 0)
        l.addWidget(self.use_progress_bar, 3, 1, Qt.AlignmentFlag.AlignCenter)

        self.setLayout(l)

    def set_schedule_func(self):
        if self.set_schedule.currentText() == "Run Periodically":
            self.set_schedule_widget.setEnabled(True)
        else:
            self.set_schedule_widget.setEnabled(False)

    def set_py_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Python File", "", "Python Files (*.py)")
        self.py_file_label.setText(file_path)

    def set_py_interpeter(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Python Interpreter", "", "Python (python.exe)")
        if file_path:
            self.py_interpreter_label.setText(file_path)
        else:
            QMessageBox.critical(self, "Invalid Interpreter", "A valid Python Interpreter wasn't select, defaulting to the base environment")


    def create_process(self):
        if not self.py_file_label.text():
            QMessageBox.critical(self, "Run File not Chosen", "You must select a Python file to run before creating a process.")
            return
        if not self.py_interpreter_label.text():
            QMessageBox.critical(self, "Interpreter not Chosen", "You must select a Python Interpreter to run before creating a process.")
            return
        
        text, ok = QInputDialog.getText(self, "Process Name", "Enter a Name for Process")
        if ok and text:

            self.run_data = ProcessInfo(text, self.py_file_label.text(), 
                                        self.py_interpreter_label.text(),
                                        self.set_schedule.currentText(), 
                                        self.use_progress_bar.isChecked(),
                                        {"time_unit":self.set_schedule_widget.time_value_set.currentText(), 
                                         "value": self.set_schedule_widget.value_input.text()})

            self.create_process_ready.emit()
        elif ok:
            QMessageBox.critical(self, "Process Name not given", "Your process must have a name.")







