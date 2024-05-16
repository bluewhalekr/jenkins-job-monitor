from service import mon_db


class JobStatus(mon_db.Model):
    __tablename__ = "jobstatus"
    id = mon_db.Column(mon_db.Integer, primary_key=True, autoincrement=True)
    name = mon_db.Column(mon_db.String(128))
    execution_id = mon_db.Column(mon_db.Integer)
    execution_time = mon_db.Column(mon_db.Integer)
    execution_duration = mon_db.Column(mon_db.Integer)
    status = mon_db.Column(mon_db.String(16))

    def __init__(self, **kwargs):
        super(JobStatus, self).__init__(**kwargs)
  
    def __str__(self) -> str:
        return f"{self.name}, {self.execution_id}, {self.execution_time}, {self.execution_duration}, {self.status}"
