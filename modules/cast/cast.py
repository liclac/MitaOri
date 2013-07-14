from flask import Blueprint, render_template
from models import *

mod = Blueprint('cast', __name__,
				template_folder='templates')

@mod.route('/')
def index():
	categories = CharacterCategory.query.all()
	return render_template('cast/index.html', categories=categories)
