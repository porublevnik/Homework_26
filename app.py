from flask import Flask
from views import main_bp
from db import db
from config import config

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app

app = create_app(config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=25000)