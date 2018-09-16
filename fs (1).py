class User:
    def __init__(self, first_name, last_name, ID, password, user_name, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.password = password
        self.user_name = user_name
        self.mail = mail
    
    def setfirst_name(self, first_name):
        if first_name != "":
            self.first_name = first_name
            return self.first_name
        
    def getfirst_name(self, first_name):
        if first_name != "":
            self.first_name = first_name
            return self.first_name

    def setlast_name(self, last_name):
        if last_name != "":
            self.last_name = last_name
            return self.last_name

    def getlast_name(self, last_name):
        if last_name != "":
            self.last_name = last_name
            return self.last_name   

    def setID(self, ID):
        if ID != "":
            self.ID = ID
            return self.ID

    def getID(self, ID):
        if ID != "":
            self.ID = ID
            return self.ID

    def setpassword(self, password):
        if password != "":
            self.password = password
            return self.ID

    def getpassword(self, password):
        if password != "":
            self.password = password
            return self.password

    def setuser_name(self, user_name):
        if user_name != "":
            self.user_name = user_name
            return self.user_name

    def getuser_name(self, user_name):
        if user_name != "":
            self.username = user_name
            return self.user_name

    def setmail(self, mail):
        if mail != "":
            self.mail = mail
            return self.user_name

    def getmail(self, mail):
        if mail != "":
            self.mail = mail
            return self.mail
        
  
class Student(User):

    def __init__(self, first_name, last_name, ID, password, user_name, mail, courses, assignments):
        self.courses = courses
        self.assignments = assignments
        self.grade = []
        super(Student, self).__init__()

    def setcourses(self, courses):
        self.courses = courses
        return self.courses

    def getcourses(self, courses):
        self.courses = courses
        return self.courses

    def setgrade(self, grade):
        self.grade = grade
        return self.grade

    def setassignments(self, assignment):
        self.assignments = assignments
        return self.assignments

    def getassignments(self, assignments):
        self.assignments = assignments
        return self.assignments

    def displayStudent(self):
        print ("Student name is " + self.firstname + " " + self.lastname + " " + self.id)


    def displayGrade(self):
        for grade in self.grade:
            print (grade.course.name + ": " + grade.assignments.name + ": " + str(grade.grade.__mark__)

            
    
class Lecturer(User):

    def __init__(self, first_name, last_name, ID, password, user_name, mail, courses, assignments)
        self.courses = courses
        self.assignments = assignments
        super(Lecturer, self).__init__()

    def setcourses(self, courses):
        self.courses = courses
        return self.courses

    def getcourses(self, courses):
        self.courses = courses
        return self.courses

    def setassignments(self, assignment):
        self.assignments = assignments
        return self.assignments

    def getassignments(self, assignments):
        self.assignments = assignments
        return self.assignments


class Grade:
    __min__ = 0
    __max__ = 100

    def __init__(self, mark):
        self.__mark__ = mark
        
    def setgrade(self, grade):
        return self.grade

    def getgrade(self, grade):
        return self.grade

    def checkIfValid(self):
        return self

class Course:

    def __init__(self, name, ID, credit, lecturer, assignments):
          self.name = name
          self.ID = ID
          self.credit = credit
          self.lecturer = lecturer
          self.assignments = []


    def setname(self, name):
        return self.title

    def getname(self, name):
        return self.name

    def _setID_(self, ID):  
        return self.ID

    def _getID_(self, ID):  
        return self.ID

    def _setcredit_(self, credit):
        return self.credit

    def _getcredit_(self, credit):  
        return self.credit

    def _setlecturer_(self, lecturer):  
        return self.lecturer

    def _getlecturer_(self, lecturer):  
        return self.lecturer

    def _setassignments_(self, assignments):  
        return self.assignments

    def _getassignments_(self, assignments):  
        return self.assignments

class Assignment:
    min = 0
    max = 5
    
    def __init__(self, name, percent, grade, deadline, status, description):
        self.name = name
        self.percent = percent
        self.grade = grade
        self.deadline = deadline
        self.status = status
        self.description = description
        
    def setName(self, name):
        return self.name

    def _getname_(self, name):
        return self.name

    def _setpercent_(self, percent):
        return self.percent

    def _getpercent_(self, percent):
        return self.percent

    def _setgrade_(self, grade):
        return self.grade

    def _getgrade_(self, grade):
        return self.grade

    def setdeadline(self, deadline):
        return self.deadline

    def getdeadline(self, deadline):
        return self.deadline

    def _setstatus_(self, status):
        return self.status

    def _getstatus_(self, status):
        return self.status

    def _setdescription_(self, description):
        return self.description

    def _getdescription_(self, description):
        return self.description

    def CkeckIfLate(self): 
        return self

    def CheckIfGraded(self): 
        return self

class AssignmentGrade:
    def __init__(self, course, assignment, grade):
        self.course = course
        self.assignment = assignment
        self.grade = Grade(grade)
        self.state = 0

    

def main(self):
    cA = Course("Data Structures", "ENGS115", "4", "Satenik", "5")

    asgnA = Assignment("Assignment1", "AssignAText", 20, "2018-09-16", "ABC", "Descr")
    asgnB = Assignment("Assignment1", "AssignBText", 20, "2018-09-16", "ABC", "Descr")
    cA.assignment.append(asgnA, asgnB)

    stA = Student("Meri", "Balasanyan", "AUA789", "meri_balasanyan", "*********", "6", "20")
    stA.courses.append(cA)

    asgrade1 = AssignmentGrade(cA, asgnA, 95)
    asgrade2 = AssignmentGrade(cA, asgnB, 92)
    stA.grades.append(asgrade1)
    stA.grades.append(asgrade2)

    asgnA.name = "Assignment1"
    asgnB.name = "Assignment2"

    st1.displayGrades()

    
main()
