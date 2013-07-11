import datetime
from flask import Blueprint, Response, render_template, jsonify, url_for
from sqlalchemy import func, orm
from models import *
from cache import FileCache

mod = Blueprint('log', __name__,
				template_folder='templates')
cache = FileCache('log')

def get_dates():
	query = db.session.query(func.DATE(Post.posted)).distinct()
	return [ date[0] for date in query.all() ]

@mod.route('/')
def index():
	dates = get_dates()
	return render_template('log/index.html', dates=dates)

@mod.route('/<int:year>/<int:month>/<int:day>/')
def day(year, month, day):
	date = datetime.date(year, month, day)
	key = date.strftime('%Y_%m_%d')
	data = cache.get(key)
	if not data:
		data = {
			'posts': Post.query.filter(func.DATE(Post.posted) == date).options(orm.subqueryload('character')).all(),
			'back_date': db.session.query(func.DATE(Post.posted)).filter(Post.posted < date).order_by(Post.posted.desc()).first()[0],
			'next_date': db.session.query(func.DATE(Post.posted)).filter(Post.posted > (date + datetime.timedelta(days=1))).order_by(Post.posted).first()[0]
		}
		cache.set(key, data)
	return render_template('log/day.html', date=date, posts=data['posts'], back_date=data['back_date'], next_date=data['next_date'])

@mod.route('/data/characters.css')
def data_characters_css():
	characters = Character.query.all()
	return Response(render_template('log/characters.css', characters=characters), mimetype="text/css")
