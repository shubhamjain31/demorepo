class Property:
	def __init__(self, var):
		self.s = var
		
	@property
	def s(self):
		return self.__s
		
	@s.setter
	def s(self, var):
		if var > 0 and var % 2 == 0:
			self.__s = var
		else:
			self.__s = 2
		
obj = Property(23)
print(obj.s)