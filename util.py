import os

def path_for(p):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), p)
