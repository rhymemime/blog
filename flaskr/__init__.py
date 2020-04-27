import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

app.config.from_pyfile('config.py', silent=True)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from . import db
db.init_app(app)

from . import auth
app.register_blueprint(auth.bp)

from . import blog
app.register_blueprint(blog.bp)

from . import landing
app.register_blueprint(landing.bp)
app.add_url_rule('/', endpoint='index')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

#return app
