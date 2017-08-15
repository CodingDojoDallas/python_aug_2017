#students = [
     #{'first_name':  'Michael', 'last_name' : 'Jordan'},
    # {'first_name' : 'John', 'last_name' : 'Rosales'},
     #{'first_name' : 'Mark', 'last_name' : 'Guillen'},
    # {'first_name' : 'KB', 'last_name' : 'Tonel'}
#]
#for student in students:
    
   #print student['first_name'] + ' ' + student ['last_name']

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def students_and_teachers(obj):
    for key in obj:
      print key
    for value in obj.iteritems():
      print '{}'.format(key)