class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

#Getters
  def getName(self):
    return self.name 
  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents
#Setters
  def setNumberOfStudents(self, new_number):
    self.numberOfStudents = new_number


  

  def __repr__(self):
    return 'A {level} school named {name} with {numberOfStudents} students.'.format(level = self.level, name = self.name, numberOfStudents = self.numberOfStudents)

a = School("Codecademy", "high", 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(200)
print(a.getNumberOfStudents())

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    self.name = name
    self.numberOfStudents = numberOfStudents
    self.pickupPolicy = pickupPolicy
    super().__init__(name, 'primary', numberOfStudents)
#getters
  def getPickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup policy is: {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

b = PrimarySchool('44', 33, '"with parents only".')
print(b.getPickupPolicy())
print(b)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    name = super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams


#getters
  def getSportsTeams(self):
    return self.sportsTeams 
  def __repr__(self):
    return super().__repr__() + f". Sports teams: {', '.join(self.sportsTeams)}"


c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.getSportsTeams())
print(c)

