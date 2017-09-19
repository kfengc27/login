from flask_login import UserMixin

class User(UserMixin):
	def __init__(self,id):
		self.id = id

	def get_id(self):
		return self.id

	def is_authenticated():
		return tree 

	def is_anonymous():
		return true 

	def is_active():
	 	return true


