from config import Config
from flask_sqlalchemy import SQLAlchemy

mon_db = SQLAlchemy()


def init(flask_app):
    global mon_db
    print(f'db_path = {Config.Db.db_file}')
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + Config.Db.db_file
    flask_app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    mon_db.init_app(flask_app)
    mon_db.app = flask_app
    mon_db.create_all()


def fint():
    global mon_db
    if mon_db is not None:
        mon_db.session.close()
        mon_db = None
