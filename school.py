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