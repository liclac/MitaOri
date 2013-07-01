import datetime
from flask import Blueprint, render_template
from sqlalchemy import func, orm
from models import *

mod = Blueprint('log', __name__,
				template_folder='templates')

@mod.route('/')
def index():
	query = db.session.query(func.DATE(Post.posted)).distinct()
	dates = [ date[0] for date in query.all() ]
	return render_template('log/index.html', dates=dates)

@mod.route('/<int:year>/<int:month>/<int:day>/')
def day(year, month, day):
	date = datetime.date(year, month, day)
	query = Post.query.filter(func.DATE(Post.posted) == date).options(orm.subqueryload('character'))
	posts = query.all()
	# Failed attempt to preload characters, leaving for later
	#character_ids = set(post.character_id for post in posts)
	#list(Character.query.filter(Character.id.in_(character_ids)))
	return render_template('log/day.html', date=date, posts=posts)
