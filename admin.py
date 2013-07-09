from wtforms.fields import TextField
#from flask.ext.login import current_user
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqlamodel import ModelView
from models import db, Character, Post, WikiPage

admin = Admin()

class MitaOriModelView(ModelView):
	model = None
	
	def __init__(self, *args, **kwargs):
		super(MitaOriModelView, self).__init__(self.model, *args, **kwargs)
	
	#def is_accessible(self):
	#	return current_user.is_authenticated() and current_user.is_admin

class CharacterAdminView(MitaOriModelView):
	model = Character

class PostAdminView(MitaOriModelView):
	model = Post
	form_overrides = {'reply_to': TextField}
	column_list = ['character', 'text', 'posted', 'reply_to']

class WikiPageAdminView(MitaOriModelView):
	model = WikiPage

admin.add_view(CharacterAdminView(db.session, name="Characters", endpoint="characters"))
admin.add_view(PostAdminView(db.session, name="Posts", endpoint="posts"))
admin.add_view(WikiPageAdminView(db.session, name="Wiki", endpoint="wiki_pages"))
