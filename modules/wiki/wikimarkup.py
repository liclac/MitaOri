import re
import markdown2
from flask import url_for
from models import *

_link_exp = re.compile(r'\[\[([^\]]+)\]\]')
def _link_replacement(match):
	linkparts = match.group(1).split('|')
	page = linkparts[0].replace(' ', '_')
	title = linkparts[1] if len(linkparts) > 1 else linkparts[0].replace('_', ' ')
	url = url_for('wiki.page', title=page)
	return "[%s](%s)" % (title, url)

def wikify(s):
	s = _link_exp.sub(_link_replacement, s)
	return markdown2.markdown(s)
