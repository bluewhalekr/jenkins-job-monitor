class ScheduleJob:
    def __init__(self, name, hour, minutes, seconds, job_type):
        self._hour = hour
        self._seconds = seconds
        self._minutes = minutes
        self._name = name
        self._job_type = job_type

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def seconds(self) -> int:
        return self._seconds

    @property
    def minutes(self) -> int:
        return self._minutes

    @property
    def name(self) -> str:
        return self._name

    @property
    def job_type(self) -> str:
        return self._job_type

    @hour.setter
    def hour(self, val: int):
        self._hour = val

    @seconds.setter
    def seconds(self, val: int):
        self._seconds = val

    @minutes.setter
    def minutes(self, val: int):
        self._minutes = val
    
    @name.setter
    def name(self, val: str):
        self._name = val

    @job_type.setter
    def job_type(self, val: str):
        self._job_type = val

    def execute(self):
        self.__operate__()

    def __operate__(self):
        pass
