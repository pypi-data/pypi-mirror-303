from .schedule_objects import RunIndefinitely, RunPeriodically
from PySide6.QtCore import QProcess

from datetime import datetime
import pathlib
import sys


class PyProcess(QProcess):
    def __init__(self, process_name:str, py_interpreter_path:str, py_run_file:str, schedule:RunIndefinitely | RunPeriodically) -> None:
        super().__init__()

        self.__name = process_name
        self.__py_interpreter_path:str = py_interpreter_path
        self.__py_run_file:str = py_run_file
        self.__schedule:RunIndefinitely | RunPeriodically = schedule

        self.py_env_name = self.get_env_name()

    @property
    def scheudule_type(self):
        return type(self.__schedule)
    @property
    def schedule_name(self) -> str:
        return self.__schedule.name
    @property
    def is_ready(self) -> bool:
        if type(self.__schedule) == RunIndefinitely:
            if self.process_id:
                return False
            else:
                return True
        else:
            return datetime.now() >= self.__schedule.next_run
    
    @property
    def process_id(self) -> int:
        return self.processId()
    @property
    def name(self):
        return self.__name
    @property
    def run_file_name(self) -> str:
        return pathlib.Path(self.__py_run_file).name

    @property
    def next_run_in(self) -> str:
        if self.process_id:
            return "Running"
        else:
            return f"{str(self.__schedule.next_run_in).split('.')[0]}"
    @property
    def run_duration(self) -> str:
        if not self.process_id:
            return "Until Next Run"
        else:
            return f"{str(self.__schedule.duration).split('.')[0]}"

    @property
    def next_scheduled_run(self) -> datetime:
        return self.__schedule.next_run
    @property
    def previous_run_time(self) -> datetime:
        return self.__schedule.start_time
    

    def run(self):
        self.start(self.__py_interpreter_path, [self.__py_run_file])
        self.__schedule.start_time = datetime.now()
        
    def get_env_name(self):
        if self.__py_interpreter_path == "python":
            return pathlib.Path(sys.prefix).name
        
        path = pathlib.Path(self.__py_interpreter_path)
        if path.parent.joinpath("conda-meta").is_dir():
            return path.parts[-1]
        else:
            if path.parent == pathlib.Path(sys.base_prefix):
                return path.parts[-2]
            else:
                return path.parts[-3]


