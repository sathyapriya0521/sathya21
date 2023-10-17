'''
Implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function 
with different input lists of students.
'''

class student:
    
def__init__(self,name,roll_number,cgpa):
self.name=name
self.roll_number=roll_number
self.cgpa-cgpa


def sort_students(students_list):
  #sort the list of students in descending order of cgpa
  sorted_students = sorted(students_list,
                           key=lambda student: student.cgpa,
                           reverse=true)
 #syntax - lambda arg:exp
  return sorted_students
  

#example usage:
students=[
  student("Hari", "A123", 7.8),
  student("Srikanth","A124",8.9),
  student("saumya", "A126",9.1),
  student("Mahidhar", "A125",9.9),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name:{}", Roll number:{}, CGPA: {}".format(student.name,
  students.roll_number,
                                      student.cgpa))