import csv
from firebase import firebase

firebase = firebase.FirebaseApplication("https://tastyapp-99fc1.firebaseio.com", None)
result = firebase.get('/users', None)

print result


#with open('foodlist.csv') as f:
#
#    reader = csv.DictReader(f)
#    for row in reader:
#        print (row['ndb_number'], row['food'])

