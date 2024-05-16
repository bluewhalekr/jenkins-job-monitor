from service import mon_db
from loguru import logger
from datetime import datetime
from model.job_status import JobStatus as JobStatusModel
from view import app_handler


class JobStatus:
    @classmethod
    def del_job_status(cls, name, execution_id):
        job_status = JobStatusModel.query.filter_by(name=name, execution_id=execution_id).first()
        if job_status is not None:
            mon_db.session.delete(job_status)
            mon_db.session.commit()
        else:
            raise(Exception(f'Not found job_status.[name={name}, id={execution_id}]'))

    @classmethod
    def add_new_job_status(cls, name, execution_id, execution_time, execution_duration, status):
        job_status = JobStatusModel.query.filter_by(name=name, execution_id=execution_id).first()
        if job_status is None:
            job_status = JobStatusModel(name=name, execution_id=execution_id, execution_time=execution_time, execution_duration=execution_duration, status=status)
            mon_db.session.add(job_status)
            mon_db.session.commit()

    @classmethod
    def get_job_status_by_exec_time(cls, name, interval_sec: int) -> JobStatusModel:
        import time
        allowed = time.time() - float(interval_sec)
        
        job_status = JobStatusModel.query.filter(JobStatusModel.name==name).filter(JobStatusModel.execution_time>=allowed).first()

        if job_status is not None:
            return job_status

        return None

    @classmethod
    def get_job_status_all_by_exec_time(cls, interval_sec: int) -> JobStatusModel:
        import time
        allowed = time.time() - float(interval_sec)
        
        job_status = JobStatusModel.query.filter(JobStatusModel.execution_time>=allowed).all()

        if job_status is not None:
            return job_status
        else:
            logger.info(f'get_job_status_all_by_exec_time, result=None, interval_sec = {interval_sec}')
    
        return None

    @staticmethod
    def str_to_class(job_name: str, lines: str):
        if len(lines) > 0:
            lines = lines.replace('\n', '')
            cols = lines.split(',')
            if len(cols) == 4:
                exec_timestamp = int(cols[1])
                exec_dt = datetime.fromtimestamp(exec_timestamp/1000)
                JobStatus.add_new_job_status(name=job_name, execution_id=cols[0], execution_time = exec_dt, execution_duration=cols[2], status=cols[3])
