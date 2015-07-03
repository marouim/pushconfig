__author__ = 'martin'


import json


newtable = {}

newtable['devices'] = []

with open('devices.txt', mode='r') as fdev:
    for rawline in fdev:
        line = rawline.rstrip('\n')
        split =  line.split()
        hostname = split[1]
        ipaddress = split[0]
        print ("hostname: %s ipaddress: %s" % (hostname, ipaddress))

        item = {u'hostname': unicode(hostname), u'ipaddress': unicode(ipaddress), u'model': u'cisco'}

        newtable['devices'].append(item)


print (json.dumps(newtable))
