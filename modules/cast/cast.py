from flask import Blueprint, render_template
from models import *

mod = Blueprint('cast', __name__,
				template_folder='templates')

@mod.route('/')
def index():
	characters = Character.query.all()
	return render_template('cast/index.html', characters=characters)
