from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	nickname = db.Column(db.String(20))
	username = db.Column(db.String(15), unique=True)
	avatar_url = db.Column(db.Text)
	bio = db.Column(db.Text)
	color = db.Column(db.String(6))
	category_id = db.Column(db.Integer, db.ForeignKey('character_category.id'), nullable=True)
	category = db.relationship('CharacterCategory', backref=db.backref('characters', lazy='dynamic'))
	
	def __str__(self):
		return self.name

class CharacterCategory(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	weight = db.Column(db.Integer, nullable=False, default=0)
	
	def __str__(self):
		return "[%s] %s" % (self.weight, self.title)

class Post(db.Model):
	id = db.Column(db.BigInteger, primary_key=True)
	character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
	character = db.relationship('Character', backref=db.backref('entries', lazy='dynamic'))
	reply_to_id = db.Column(db.BigInteger, db.ForeignKey('post.id'), nullable=True)
	reply_to = db.relationship('Post', remote_side=[id], backref=db.backref('replies'))
	posted = db.Column(db.DateTime)
	text = db.Column(db.Text)
	
	def __str__(self):
		return "%s: %s" % (self.character.nickname, self.text)

class WikiPage(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), unique=True)
	content = db.Column(db.Text)
	
	@classmethod
	def with_title(cls, title):
		return cls.query.filter_by(title=title.replace('_', ' ')).first()
	
	def __str__(self):
		return self.title
