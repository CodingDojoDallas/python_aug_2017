#set users dictionary
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

#define functions
for key,data in users.iteritems():
    print key
    counter = 0
    for value in data:
        counter += 1
        print str(counter) + ' - ' + value['first_name'].upper() + ' ' + value['last_name'].upper() + ' - ' + str(len(value['first_name']) + len(value['last_name']))
