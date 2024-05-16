import requests
from config import Config


class JobStatus:
    @classmethod
    def request_add_job_status(cls, name, exec_id, exec_time, exec_dur, status):
        uri = f'http://{Config.Http.addr}:{Config.Http.port}/jobstatus'
        data = {'name': name, 'id': exec_id, 'time': exec_time, 'dur': exec_dur, 'status': status}
        
        requests.post(uri, json=data)
    
    @classmethod
    def add_line_to_job_status(cls, name, line):
        if len(line) > 0:
            line = line.replace('\n', '')
            cols = line.split(',')
            if len(cols) == 4:
                exec_timestamp = int(cols[1])
                cls.request_add_job_status(name=name, exec_id=cols[0], exec_time=exec_timestamp / 1000, exec_dur=cols[2], status=cols[3])
    
    @classmethod
    def add_line_to_job_status_1(cls, name, next_id, exec_ts):
        cls.request_add_job_status(name=name, exec_id=next_id, exec_time=exec_ts, exec_dur="0", status="SUCCESS")
