class CGPA(ABC):
  def __init__(self):
    pass
  @abstractmethod
  def getCGPA(self):
    print('YOUR CGPA OF ALL COURSES IS WRITTEN BELOW.')

class stud_A(CGPA):
  def __init__(self,course1,course2,course3):
    self.course1 = course1
    self.course2 = course2
    self.course3 = course3
  def getCGPA(self):
    print('YOUR CGPA OF ALL COURSES IS WRITTEN BELOW.')
  def cal_gpa(self):
    total = (self.course1 + self.course2 + self.course3)/3
    total1 = float("{0:.2f}".format(total))
    print('YOUR TOTAL MARKS:',total1)
    if total == 100 and total > 85 :
      print('YOUR GPA IS 4 AND YOUR GRADE IS A.')
    elif total < 84 and total > 70 :
      print('YOUR GPA IS 3 AND YOUR GRADE IS B.')
    elif total < 69 and total > 55 :
      print('YOUR GPA IS 2 AND YOUR GRADE IS C.')
    elif total < 54 and total > 40 :
      print('YOUR GPA IS 1 AND YOUR GRADE IS D.')
    elif total < 39 and total >= 0 :
      print('YOUR GPA IS 0 AND YOUR GRADE IS F.')
def Final(GPA):
  GPA.getCGPA()
  GPA.cal_gpa()

class stud_B(CGPA):
  def __init__(self,course1,course2,course3,course4):
    self.course1 = course1
    self.course2 = course2
    self.course3 = course3
    self.course4 = course4

  def getCGPA(self):
    print('YOUR CGPA OF ALL COURSES IS WRITTEN BELOW.')
  def cal_gpa(self):
    total = (self.course1 + self.course2 + self.course3 + self.course4)/4
    print('YOUR TOTAL MARKS:',total)
    if total == 100 and total > 85 :
      print('YOUR GPA IS 4 AND YOUR GRADE IS A.')
    elif total < 84 and total > 70 :
      print('YOUR GPA IS 3 AND YOUR GRADE IS B.')
    elif total < 69 and total > 55 :
      print('YOUR GPA IS 2 AND YOUR GRADE IS C.')
    elif total < 54 and total > 40 :
      print('YOUR GPA IS 1 AND YOUR GRADE IS D.')
    elif total < 39 and total >= 0 :
      print('YOUR GPA IS 0 AND YOUR GRADE IS F.')
  
def Final(GPA):
  GPA.getCGPA()
  GPA.cal_gpa()

course1 = eval(input('ENTER MARKS OF OOP COURSE: '))
course2 = eval(input('ENTER MARKS OF DLD COURSE: '))
course3 = eval(input('ENTER MARKS OF DS COURSE: '))
student1 = stud_A(course1,course2,course3)
Final(student1)
print('')
course1 = eval(input('ENTER MARKS OF OOP COURSE: '))
course2 = eval(input('ENTER MARKS OF DLD COURSE: '))
course3 = eval(input('ENTER MARKS OF DS COURSE: '))
course4 = eval(input('ENTER MARKS OF OC COURSE: '))
student2 = stud_B(course1,course2,course3,course4)
Final(student2)
