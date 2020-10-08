class Geeks:
	def __init__(self, id):
		self.id = id
		
manager = Geeks(100)
manager.__dict__['life'] = 49
print(manager.life)
print(manager.life+len(manager.__dict__))