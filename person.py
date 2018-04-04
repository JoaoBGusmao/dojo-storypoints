class Person(object):
	def __init__(self, name, storyPointsDay):
		self.name = name
		self.storyPointsDay = storyPointsDay

	def getName(self):
		return self.name

	def getStoryPointsDay(self):
		return self.storyPointsDay

# team = [Person("Joao", 8), Person("Vinna", 8), Person("Jon", 13)]

# for person in team:
# 	print(person.getName())
