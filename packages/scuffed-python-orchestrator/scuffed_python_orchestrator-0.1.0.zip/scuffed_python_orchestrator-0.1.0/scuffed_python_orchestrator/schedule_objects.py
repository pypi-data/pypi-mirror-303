from datetime import datetime, timedelta


class RunIndefinitely:
    def __init__(self, start_time=datetime.fromtimestamp(0)) -> None:
        self.start_time:datetime = start_time

    @property
    def name(self) -> str:
        return "Runs Indefinitely"
    
    @property
    def next_run(self) -> datetime:
        return self.start_time

    @property
    def next_run_in(self) -> timedelta:
        return timedelta(seconds=0)
    
    @property
    def duration(self) -> timedelta:
        return datetime.now() - self.start_time
       
class RunPeriodically:
    def __init__(self, periodcity:timedelta, start_time=datetime.fromtimestamp(0)) -> None:
        self.start_time:datetime = start_time
        self.periodicity:timedelta = periodcity

    @property
    def name(self):
        return f"Runs every {self.periodicity}"
    
    @property
    def next_run(self) -> datetime:
        return self.start_time + self.periodicity

    @property
    def next_run_in(self) -> timedelta:
        return self.next_run - datetime.now()
    
    @property
    def duration(self) -> timedelta:
        return datetime.now() - self.start_time



  