import os
import sys
import signal
import loguru
from schedule.schedule import init as schedule_init
from schedule.schedule import run as schedule_run
from view import init as view_init
from view import run as view_run
from service import init as service_init

PID_FILE = "/var/run/jenkins-job-mon.pid"


def sig_handler(signum, frame):
    if signum in [signal.SIGTERM, signal.SIGINT]:
        exit()


def __init(is_daemon: bool):
    loguru.logger.add("/opt/jenkins-job-mon/log/{time}.log", rotation='10MB', compression='zip', retention='5 days')
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)
    schedule_init(is_daemon=is_daemon)
    flask_app = view_init()
    with flask_app.app_context():
        service_init(flask_app)
    return flask_app


def __run():
    schedule_run()
    view_run()


def __daemonize():
    pid = os.fork()
    if pid > 0:
        exit(0)
    else:
        os.chdir("/")
        os.setsid()
        os.umask(0)
        pid = os.fork()
        if pid > 0:
            exit(0)
        else:
            # sys.stdin.flush()
            # sys.stdout.flush()
            si = open(os.devnull, 'r')
            so = open(os.devnull, 'a+')
            se = open(os.devnull, 'a+')
            
            os.dup2(si.fileno(), sys.stdin.fileno())
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())
            
            with open(PID_FILE, "wt") as fp:
                fp.write(str(os.getpid()))
                fp.close()
                __init(is_daemon=True)
                __run()


def main():
    is_daemon: bool = False
    
    if len(sys.argv) > 1 and sys.argv[1] == "-d":
        is_daemon = True
    
    if is_daemon:
        __daemonize()
    else:
        __init(is_daemon=True)
        __run()


if __name__ == "__main__":
    main()
