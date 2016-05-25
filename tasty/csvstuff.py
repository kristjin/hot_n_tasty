#import csv

#with open('foodlist.csv') as f:
#
#    reader = csv.DictReader(f)
#    for row in reader:
#        print (row['ndb_number'], row['food'])

from firebase import firebase
auth = firebase.FirebaseAuthentication('FIREBASE_SECRET', 'firebase@firebase.com')
firebase = firebase.FirebaseApplication('https://tastyapp-99fc1.firebaseio.com', auth)
result = firebase.get('/users', auth)
print result

json_dict = firebase.get('/users', '1', {'print': 'pretty'})
print json_dict


user = authentication.get_user()
print user.firebase_auth_token


result = firebase.get('/users', None, {'print': 'pretty'})
print result
