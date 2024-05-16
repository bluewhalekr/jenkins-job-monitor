from flask.views import View


class AboutView(View):
    methods = ["GET"]
    
    def dispatch_request(self):
        return {"title": "jenkins job monitor", "version": "0.0.1", "author": "aimmo"}, 200
