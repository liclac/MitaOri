from flask import Blueprint, url_for, redirect, render_template, abort
from models import *
import wikimarkup

mod = Blueprint('wiki', __name__,
				template_folder='templates')

@mod.app_template_filter()
def wikify(s):
	return wikimarkup.wikify(s)

@mod.route('/')
def index():
	return redirect(url_for('wiki.page', title='Mitakihara_Original'))

@mod.route('/<title>')
def page(title):
	if ' ' in title:
		return redirect(url_for('wiki.page', title=title.replace(' ', '_')))
	
	page = WikiPage.with_title(title) or abort(404)
	return render_template('wiki/page.html', page=page)

@mod.errorhandler(404)
def error404(e):
	return render_template('wiki/404.html')
