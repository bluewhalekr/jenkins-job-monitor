from schedule_ctx import ScheduleCtx
from schedule_job_monitor import ScheduleJobMonitor

jobs = []
_schedule_ctx: ScheduleCtx


def check_ctx(func):
    def wrapper(*args):
        if _schedule_ctx is None:
            raise(Exception("ScheduleCtx is None.({func})"))
        return func(*args)
    return wrapper


def init(is_daemon: bool):
    global jobs, _schedule_ctx
    jobs = [ScheduleJobMonitor()]

    _schedule_ctx = ScheduleCtx(is_daemon=is_daemon, jobs=jobs)


@check_ctx
def run():
    if _schedule_ctx is not None:
        _schedule_ctx.start()


@check_ctx
def stop():
    global _schedule_ctx
    if _schedule_ctx is not None:
        _schedule_ctx.stop()
        _schedule_ctx = None
