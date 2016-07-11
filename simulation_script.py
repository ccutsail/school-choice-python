import networkx as nx

import matplotlib.pyplot as plt

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

student_list = []

for k in stud_list:
    sk = "S" + str(k)
    student_list[len(student_list):] = [sk]

G = nx.Graph()
G2 = nx.MultiDiGraph()
G.add_nodes_from ( student_list,bipartite = 0)
G.add_nodes_from ( num_schools,bipartite = 1)

G2.add_nodes_from ( student_list )
G2.add_nodes_from ( num_schools )


for k in stud_list:
    G.add_edge(student_list[k],stableMarriage(students,schools)[k])

for k in stud_list:
    G2.add_edge(student_list[k],students[k].prefList[0])
    
### Positioning doesn't work properly in NetworkX. 
### Use Sage for visualization. Script is almost identical -- 
### Just copy and paste, get rid of reading and writing
    
    
l = student_list
r = num_schools
pos = {}

# UpG2.add_nodes_from ( stud_list,bipartite = 0)date position for node from each group
pos.update((node, (1, index)) for index, node in enumerate(l))
pos.update((node, (2, index)) for index, node in enumerate(r))
# pos = nx.spring_layout(G,k=0.15,iterations=20)
nx.write_graphml(G,"/Users/corycutsail/Desktop/Summer 16/matching/simulassignment.graphml")
G = nx.read_graphml("/Users/corycutsail/Desktop/Summer 16/matching/simulassignment.graphml")

nx.write_graphml(G2,"/Users/corycutsail/Desktop/Summer 16/matching/preTTC.graphml")
G2 = nx.read_graphml("/Users/corycutsail/Desktop/Summer 16/matching/preTTC.graphml")

plt.figure(1)
nx.draw(G,with_labels=True,node_color='white')
plt.show()

plt.figure(2)
nx.draw(G2,with_labels=True,node_color='white')
plt.show()

