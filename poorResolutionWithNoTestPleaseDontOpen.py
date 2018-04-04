from person import Person
import datetime

littleFatness = 1
projectDemands = [8, 3, 5, 13, 2, 2, 1, 5, 13, 20]

team = [Person("Joao", 8), Person("Vinna", 8), Person("Jon", 13)]

#Sum of project points
projectSum = 0
for point in projectDemands:
	projectSum = projectSum + point

#Team effort by day
effortByDay = 0 #Reality
for person in team:
	effortByDay = effortByDay + person.getStoryPointsDay()

#Days needed
daysNeeded = (projectSum // effortByDay) + littleFatness
today = datetime.datetime.utcnow()

endDate = today + datetime.timedelta(days=daysNeeded)

print(endDate)