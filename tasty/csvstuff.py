#import csv

#with open('foodlist.csv') as f:
#
#    reader = csv.DictReader(f)
#    for row in reader:
#        print (row['ndb_number'], row['food'])
import ConfigParser

cfg = ConfigParser.RawConfigParser()
cfg.read('tasty.cfg')
FIREBASE_SECRET = cfg.get("firebase", "secret")


from firebase import firebase as fb

auth = fb.FirebaseAuthentication(FIREBASE_SECRET, 'shithead@ssss.com')
fb.authentication = auth
print auth.extra

tastydb = fb.FirebaseApplication('https://tastyapp-99fc1.firebaseio.com', auth)

result = tastydb.get('/matchlist', None)
print "The get result of all /matchlist is:"
print result

user = auth.get_user()
print user.firebase_auth_token
print user.email
print user.id
print user.provider


