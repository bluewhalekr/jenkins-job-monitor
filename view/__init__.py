from flask import Flask
from config import Config

app_handler = None


def chk_handler(func):
    def wrapper(*args):
        if app_handler is None:
            raise (Exception(f'flask handler is None. {func}'))
        func(*args)
    
    return wrapper


def init():
    global app_handler
    from view.aboutview import AboutView
    from view.metricview import MetricView
    from view.jobstatusview import JobStatusView
    
    app_handler = Flask('jenkins-job-mon')
    
    view_list = {"/about": (AboutView, "aboutview"), "/metric/<job_name>/<interval_sec>": (MetricView, "metricview"),
                 "/jobstatus": (JobStatusView, "jobstatusview")}
    
    for view in view_list:
        app_handler.add_url_rule(view, view_func=view_list[view][0].as_view(view_list[view][1]))
    
    return app_handler


@chk_handler
def run():
    if app_handler is not None:
        app_handler.run(host="0.0.0.0", port=Config.Web.port)


@chk_handler
def fint():
    pass
