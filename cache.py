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
		if os.path.exists(path):
			with open(path, 'rb') as f:
				value = pickle.load(f)
		return value
	
	def set(self, key, value):
		path = self._path_for_key(key)
		with open(path, 'wb') as f:
			pickle.dump(value, f)
