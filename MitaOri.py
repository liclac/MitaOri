#import logging
from flask import Flask, render_template, url_for, redirect
from modules.cast import cast
from modules.log import log
from modules.wiki import wiki
from models import db
from admin import admin
from assets import assets

# Uncomment to enable database debugging
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(cast.mod, url_prefix='/cast')
app.register_blueprint(wiki.mod, url_prefix='/wiki')
app.register_blueprint(log.mod, url_prefix='/log')

db.init_app(app)
db.app = app			# Can we please have this bug fixed already?
admin.init_app(app)
assets.init_app(app)

@app.route('/')
def index():
	return wiki.page(title='Mitakihara_Original')
	#return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
