class Config:
    class ScheduleJobMonitor:
        job_list_file = "/opt/jenkins-job-mon/job_list.txt"
    
    class Web:
        port = 5054

    class Db:
        db_file = "/opt/jenkins-job-mon/monitoring.db"
    
    class Http:
        addr = "localhost"
        port = 5054
