import os
import cPickle as pickle
from util import path_for

class FileCache(object):
	base_path = path_for('cache')
	
	def __init__(self, module):
		self.base_path = os.path.join(self.base_path, module)
		if not os.path.exists(self.base_path):
			os.makedirs(self.base_path)
	
	def _path_for_key(self, key):
		return os.path.join(self.base_path, key.replace('/', '_') + '.pickle')
	
	def get(self, key):
		value = None
		path = self._path_for_key(key)
		print "Loading from %s" % path
		if os.path.exists(path):
			print "-> Exists!"
			with open(path, 'rb') as f:
				value = pickle.load(f)
		else:
			print "<- ...nope."
		return value
	
	def set(self, key, value):
		path = self._path_for_key(key)
		print "Storing to %s" % path
		print value
		with open(path, 'wb') as f:
			pickle.dump(value, f)
