class Student(object):
   def __init__(self, id, prefList):
      self.prefList = prefList
      self.rejections = 0 # num rejections is also the index of the next option
      self.id = id

   def preference(self):
      return self.prefList[self.rejections]

   def __repr__(self):
      return repr(self.id)


class School(object):
   def __init__(self, id, prefList, capacity=1):
      self.prefList = prefList
      self.capacity = capacity
      self.held = set()
      self.id = id

   def reject(self):
      # trim the self.held set down to its capacity, returning the list of rejected students.

      if len(self.held) < self.capacity:
         return set()
      else:
         sortedStudents = sorted(list(self.held), key=lambda student: self.prefList.index(student.id))
         self.held = set(sortedStudents[:self.capacity])

         return set(sortedStudents[self.capacity:])

   def __repr__(self):
      return repr(self.id)
      
      
      
# stableMarriage: [Student], [School] -> {School -> [Student]}
# construct a stable (polygamous) marriage between students and schools
def stableMarriage(students, schools):
   unassigned = set(students)

   while len(unassigned) > 0:
      for student in unassigned:
         schools[student.preference()].held.add(student)
      unassigned = set()

      for school in schools:
         unassigned |= school.reject()

      for student in unassigned:
         student.rejections += 1


   marriage = list()

   for student in students:
         marriage.append(student.prefList[student.rejections])

   return marriage



import numpy
stud_list = range(0,numpy.random.choice(100, size=None, replace=True, p=None))
num_schools = range(0,4)
students = []
for student in stud_list:
     students.append(Student(student,numpy.random.choice(num_schools, size = len(num_schools), replace = False)))

schools = []

for school in num_schools:
    schools.append(School(school,numpy.random.choice(stud_list, size = len(stud_list),replace=False),len(stud_list)))
stableMarriage(students,schools)

schools[1].capacity = 3
schools[1].capacity = 3
