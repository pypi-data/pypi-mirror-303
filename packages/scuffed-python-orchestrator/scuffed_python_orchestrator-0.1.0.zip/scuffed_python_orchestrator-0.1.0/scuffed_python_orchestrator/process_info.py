from datetime import timedelta
from typing import Literal
from .schedule_objects import RunIndefinitely, RunPeriodically


SCHEDULES = Literal["Run Periodically", "Run Indefinitely"]

class ProcessInfo:
    def __init__(self, name:str, run_file:str, interpreter:str, sched:SCHEDULES, 
                 has_progress:bool, sched_data={"time_unit":"", "value": ""}) -> None:
        self.name = name
        self.run_file = run_file
        self.interpreter = interpreter
        self.sched:SCHEDULES = sched
        self.has_progress = has_progress

        self.sched_data = sched_data
    
    @property
    def process_schedule(self) -> RunIndefinitely | RunPeriodically:
        if self.sched in ["Run Periodically", "Periodic Schedule"]:
            return RunPeriodically(self.get_periodic_run_data())
        else:
            return RunIndefinitely()

    def get_periodic_run_data(self):
        val = int(self.sched_data["value"])

        delta_map = {
            "Seconds": timedelta(seconds=val), 
            "Minutes": timedelta(minutes=val), 
            "Hours": timedelta(hours=val), 
            "Days": timedelta(days=val), 
            "Weeks": timedelta(weeks=val)
        }
        return delta_map[self.sched_data["time_unit"]]
