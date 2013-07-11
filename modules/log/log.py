import datetime
from flask import Blueprint, Response, render_template, jsonify, url_for
from sqlalchemy import func, orm
from models import *

mod = Blueprint('log', __name__,
				template_folder='templates')

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
	query = Post.query.filter(func.DATE(Post.posted) == date).options(orm.subqueryload('character'))
	posts = query.all()
	# Failed attempt to preload characters, leaving for later
	#character_ids = set(post.character_id for post in posts)
	#list(Character.query.filter(Character.id.in_(character_ids)))
	
	back_date = db.session.query(func.DATE(Post.posted)).filter(Post.posted < date).order_by(Post.posted.desc()).first()[0]
	next_date = db.session.query(func.DATE(Post.posted)).filter(Post.posted > (date + datetime.timedelta(days=1))).order_by(Post.posted).first()[0]
	return render_template('log/day.html', date=date, posts=posts, back_date=back_date, next_date=next_date)

@mod.route('/data/characters.css')
def data_characters_css():
	characters = Character.query.all()
	return Response(render_template('log/characters.css', characters=characters), mimetype="text/css")
