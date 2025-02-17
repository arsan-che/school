#defined School class with 3 attributes and 3 methods
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

#added getters
  def getName(self):
    return self.name 
  def getLevel(self):
    return self.level
  def getNumberOfStudents(self):
    return self.numberOfStudents
#added setters
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

#defined PrimarySchool class inheriting from School class with 3 attributes and 1 method
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

#defined HighSchool class inheriting from School class with 3 attributes and 1 method
print(c)

