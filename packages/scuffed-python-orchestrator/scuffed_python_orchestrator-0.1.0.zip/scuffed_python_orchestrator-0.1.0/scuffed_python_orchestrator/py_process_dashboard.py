from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QSpacerItem, QProgressBar, QPlainTextEdit
from PySide6.QtCore import Qt

from .py_process import PyProcess

PROCESS_NAME = """
font-size: 16pt; 
font-weight: bold; 
color: rgb(215,215,215);
"""
ENV_NAME = """
font-size: 8pt; 
font-weight: bold; 
color: rgb(215,215,215);
"""
RUN_TIME_INFO = """
font-size: 10pt; 
color: rgb(215,215,215);
"""

PROGRESS_BAR = """
QProgressBar{
    min-height: 10px;
    max-height: 10px;
    color: rgb(215,215,215);
    background-color: rgb(25,25,25);
    border: 2px solid rgb(55,55,55);
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    min-height: 10px;
    max-height: 10px;
    background-color: rgb(6,74,33);
    border-style: outset;
    border-radius: 3px;
}
"""
PROGRESS_LOG = """
color: rgb(215,215,215); 
background-color: rgb(30,30,30); 
border: 2px solid rgb(55,55,55); 
border-radius: 6px;
"""

class PyProcessDashboard(QWidget):
    def __init__(self, py_process:PyProcess, has_progress_steps:bool=False) -> None:
        super().__init__()

        self.__py_process = py_process
        self.__has_prog_steps = has_progress_steps

        if self.__has_prog_steps:
            self.__py_process.readyReadStandardOutput.connect(self.read_stdout)

        self.name_label = QLabel(f"{self.__py_process.name}")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        self.name_label.setStyleSheet(PROCESS_NAME)


        INFO_LABEL = f"""Runs {self.__py_process.run_file_name} using {self.__py_process.py_env_name}\n{self.__py_process.schedule_name}"""
        self.process_info_label = QLabel(INFO_LABEL)
        self.process_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.process_info_label.setStyleSheet(ENV_NAME)

        # self.countdown_label = QLabel(f"{self.__py_process.next_run_in} {self.__py_process.run_duration}")
        self.countdown_label = QLabel(f"-")
        self.countdown_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.countdown_label.setStyleSheet(RUN_TIME_INFO)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(PROGRESS_BAR)
        self.progress_bar.setMinimum(0)


        self.process_log = QPlainTextEdit()
        self.process_log.setMaximumHeight(300)
        self.process_log.setReadOnly(True)
        self.process_log.setStyleSheet(PROGRESS_LOG)

        l = QVBoxLayout()
        l.addWidget(self.name_label)
        l.addWidget(self.process_info_label)
        l.addWidget(self.countdown_label)
        l.addItem(QSpacerItem(0, 5))
        l.addWidget(self.progress_bar)
        l.addWidget(self.process_log)
        
        self.setLayout(l)

    def update_countdown(self, on_kill=False):
        self.countdown_label.setText(f"{self.__py_process.next_run_in} {self.__py_process.run_duration}")
        if on_kill:
            self.countdown_label.setText(f"-")

    def message(self, s):
        self.process_log.appendPlainText(s)
    
    def clear_messages(self):
        self.process_log.clear()

    def read_stdout(self):
        data = bytes(self.__py_process.readAllStandardOutput()).decode("utf8")
        try:
            self.set_progress(int(data))
        except:
            pass

    def start_progress(self):
        if self.__has_prog_steps:
            self.progress_bar.setMaximum(100)
        else:
            self.progress_bar.setMaximum(0)

    def set_progress(self, prog):
        if self.__has_prog_steps:
            self.prog_val = prog
            self.progress_bar.setValue(self.prog_val)
        else:
            self.progress_bar.setMaximum(100)