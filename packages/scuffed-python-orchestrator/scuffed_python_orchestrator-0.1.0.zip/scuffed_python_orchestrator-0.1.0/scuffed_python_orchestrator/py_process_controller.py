from PySide6.QtWidgets import QFrame, QVBoxLayout, QPushButton, QWidget, QGridLayout
from PySide6.QtCore import QThread, Signal, QObject, QProcess

import time
from datetime import datetime

from .schedule_objects import RunIndefinitely, RunPeriodically
from .py_process import PyProcess
from .py_process_dashboard import PyProcessDashboard
from .process_info import ProcessInfo

WIDGET_FRAME2 = """
#PyProcessController {
background-color: rgb(20,20,20); 
margin:3px; 
border:1px solid rgb(100, 100, 100);}
"""

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

QPushButton:disabled {
color: rgb(130,130,130);
background-color: rgb(45,45,45);
border-color: rgb(80,80,80);}
"""

class ProcessWorker(QObject):
    process_run_ready = Signal()
    def __init__(self, py_process, countdown_update):
        super().__init__()
        self.py_process:PyProcess = py_process
        self.countdown_update = countdown_update
        self.__running:bool = False
    
    def start(self):
        self.__running:bool = True
    def stop(self):
        self.__running = False

    def check_ready(self):
        if self.py_process.scheudule_type == RunIndefinitely:
            while self.__running:
                if self.py_process.state() == QProcess.NotRunning:
                    self.process_run_ready.emit()                
                self.countdown_update()
                time.sleep(0.025)

        elif self.py_process.scheudule_type == RunPeriodically:
            while self.__running:
                if self.py_process.is_ready and self.py_process.state() == QProcess.NotRunning:
                    self.process_run_ready.emit()           
                self.countdown_update()
                time.sleep(0.0025)
            


class ProcessButtonControl(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.start_run_btn = QPushButton("Start")    
        self.kill_run_btn = QPushButton("Force Kill")
        self.kill_run_btn.setEnabled(False)

        self.start_thread_btn = QPushButton("Start Thread")
        self.stop_thread_btn = QPushButton("Stop Thread")
        self.stop_thread_btn.setEnabled(False)

        self.edit_config_btn = QPushButton("Configuration")
        self.edit_config_btn.setEnabled(False)
        self.clear_msg_btn = QPushButton("Clear Messages")

        self.setStyleSheet(BUTTONS)

        l = QGridLayout()
        l.addWidget(self.start_run_btn, 0, 0)
        l.addWidget(self.kill_run_btn, 1, 0)
        l.addWidget(self.start_thread_btn, 0, 1)
        l.addWidget(self.stop_thread_btn, 1, 1)
        l.addWidget(self.edit_config_btn, 2, 0)
        l.addWidget(self.clear_msg_btn, 2, 1)


        self.setLayout(l)


class PyProcessController(QFrame):
    def __init__(self, p_info:ProcessInfo=None) -> None:
        super().__init__()
        self.setFixedHeight(525)
        self.setFixedWidth(350)

        self.setObjectName("PyProcessController")
        self.setStyleSheet(WIDGET_FRAME2)
        self.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.setLineWidth(1)

        self.p_info = p_info
        self.__py_process:PyProcess = PyProcess(self.p_info.name, self.p_info.interpreter, self.p_info.run_file, self.p_info.process_schedule)
        

        self.__py_process.finished.connect(self.process_finished)
        self.dashboard = PyProcessDashboard(self.__py_process, self.p_info.has_progress)
        self.dashboard.set_progress(0)
        
        self.btn_widget = ProcessButtonControl()
        self.btn_widget.start_run_btn.pressed.connect(self.start_process)
        self.btn_widget.kill_run_btn.pressed.connect(self.kill_process)
        self.btn_widget.start_thread_btn.pressed.connect(self.start_worker)
        self.btn_widget.stop_thread_btn.pressed.connect(self.stop_worker)
        self.btn_widget.clear_msg_btn.pressed.connect(self.dashboard.clear_messages)

        l = QVBoxLayout()
        l.addWidget(self.dashboard)
        l.addWidget(self.btn_widget)

        self.setLayout(l)

        self.process_worker = ProcessWorker(self.__py_process, self.dashboard.update_countdown)
        self.process_worker.process_run_ready.connect(self.start_process)
        self.worker_thread = QThread()
        self.process_worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.process_worker.check_ready)


    def start_process(self):
        if self.__py_process.state() == QProcess.NotRunning:
            # self.dashboard.message("Executing process.")
            self.dashboard.start_progress()
            self.__py_process.run()
            self.dashboard.update_countdown()
            self.btn_widget.start_run_btn.setEnabled(False)
            self.btn_widget.kill_run_btn.setEnabled(True)
    
    def kill_process(self):
        # self.dashboard.message("Killing Process..")
        self.__py_process.kill()
        self.__py_process.waitForFinished()

    def process_finished(self):
        self.dashboard.message(f"Process Finished at {datetime.now().strftime('%H:%M:%S %d-%b-%Y')}")
        self.dashboard.update_countdown(on_kill=True)
        self.dashboard.set_progress(0)
        self.btn_widget.kill_run_btn.setEnabled(False)
        self.btn_widget.start_run_btn.setEnabled(True)
    
    def start_worker(self):
        self.worker_thread.start()
        self.process_worker.start()
        self.btn_widget.start_thread_btn.setEnabled(False)
        self.btn_widget.stop_thread_btn.setEnabled(True)
    
    def stop_worker(self):
        self.process_worker.stop()
        self.worker_thread.quit()
        self.worker_thread.wait()
        self.btn_widget.stop_thread_btn.setEnabled(False)
        self.btn_widget.start_thread_btn.setEnabled(True)
