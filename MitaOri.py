import logging
import os
from flask import Flask, render_template, url_for
from modules.cast.cast import mod as cast_mod
from modules.log.log import mod as log_mod
from modules.wiki.wiki import mod as wiki_mod
from models import db
from admin import admin

# Uncomment to enable database debugging
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

def path_for(p):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), p)

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(cast_mod, url_prefix='/cast')
app.register_blueprint(wiki_mod, url_prefix='/wiki')
app.register_blueprint(log_mod, url_prefix='/log')

db.init_app(app)
db.app = app			# Can we please have this bug fixed already?
admin.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
