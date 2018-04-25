import sys
import json
import binascii
from Savoir import Savoir

person = {'name': 'Erik', 'lastname' : 'Lacson'}

person_json = json.dumps(person)


data_hex = binascii.hexlify(person_json)
data_json = binascii.unhexlify(data_hex)
data_dict = json.loads(data_json)


print "the hex of: " + person_json + " is " + data_hex
print "\n\n"
print "the string of: " + data_hex + " is " + person_json

print data_dict['name'] + " " + data_dict['lastname']

