from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


class JobScheduleException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ScheduleCtx:
    __jobs = []
    
    def __init__(self, is_daemon: bool = True, jobs: [] = None):
        if jobs is None:
            jobs = []
        if is_daemon:
            self.__handle = BackgroundScheduler({'apscheduler.job_defaults.max_instances': 3})
        else:
            self.__handle = BlockingScheduler()
        self.__jobs = jobs
        self.__is_daemon = is_daemon
    
    def schedule_ctx(func):
        def wrapper(self, *args, **kwargs):
            if self.__handle is None:
                raise (JobScheduleException('Scheduler Handle is None.'))
            return func(self, *args, **kwargs)
        
        return wrapper
    
    @schedule_ctx
    def start(self):
        if len(self.__jobs) == 0:
            raise (JobScheduleException('Have no jobs.'))
        for job in self.__jobs:
            if job.job_type == "interval":
                minutes = job.minutes + (job.hour if job.hour > 0 else 0) * 60
                self.__handle.add_job(job.execute, job.job_type, minutes=minutes, seconds=job.seconds)
            else:
                self.__handle.add_job(job.execute, job.job_type, hour=job.hour, minutes=job.minutes)
        self.__handle.start()
    
    @schedule_ctx
    def stop(self):
        self.__handle.close()
