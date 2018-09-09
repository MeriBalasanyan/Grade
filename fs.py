class Grade:
    # class attribute
    min = 0
    max = 100
    # instance atribute
    def __init__(self, grade):
        self.grade = grade

    # instance method
    def setGrade(self. grade):
        return self.grade

    # instance method
    def getGrade(self, grade):
        return self.grade

    # instance method
    def checkIfValid(self):
        return self
    
class Assignment:
    # class attribute
    min = 0
    max = 5

    # instance attribute
    def __init__(self, name, percent, grade, deadline, status, description):
        self.name = name
        self.percent = percent
        self.grade = grade
        self.deadline = deadline
        self.status = status
        self.description = description
        
    # instance methods
    def _set1_(self, name):
        return self.name

    def _get1_(self, name):
        return self.name

    def _set2_(self, percent):  
        return self.percent

    def _get2_(self, percent): 
        return self.percent

    def _set3_(self, grade): 
        return self.grade

    def _get3_(self, grade):  
        return self.grade

    def _set4_(self, deadline):  
        return self.deadline

    def _get4_(self, deadline):  
        return self.deadline

    def _set5_(self, status):  
        return self.status

    def _get5_(self, status):  
        return self.status

    def _set6_(self, description):  
        return self.description

    def _get6_(self, description):  
        return self.description

    def CkeckIfLate(self): 
        return self

    def CheckIfGraded(self): 
        return self


class Course:

      # instance attribute
      def __init__(self, name, ID, credit, lecturer, assignments)
      self.name = name
      self.ID = ID
      self.credit = credit
      self.lecturer = lecturer
      self.assignments = assignments
      
