__author__ = 'martin'
# -*- coding: utf-8 -*-


import json
from tabulate import tabulate
import sys
from devicelist import DeviceList


def query_yes_no(question, default="oui"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"oui": True, "o": True,
             "non": False, "n": False}
    if default is None:
        prompt = " [o/n] "
    elif default == "oui":
        prompt = " [O/n] "
    elif default == "non":
        prompt = " [o/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("SVP repondre par 'oui' ou 'non' "
                             "(ou 'o' ou 'n').\n")


fdevices = open('devices.json', mode='r')
jdevices = json.loads(fdevices.read())
fdevices.close()

devtype = raw_input("Entrez le model a deployer [cisco,ciscoswitch,ciscowap,juniper]")


j2devices = []

for dev in jdevices['devices']:
    if dev['model'] == devtype:
        j2devices.append(dev)


print "Configuration"
print (tabulate(jdevices['config'], tablefmt="fancy_grid"))
print ""
print "Devices"
# print (tabulate(jdevices['devices'], tablefmt="fancy_grid"))
print (tabulate(j2devices, tablefmt="fancy_grid"))



print ("Les commandes suivantes seront appliqués sur les device ci-haut.")

if query_yes_no("Voulez-vous continuer ?"):
    devlist = DeviceList(j2devices)
    devlist.pushconfig(jdevices['config']['commands'])

# print (jdevices)


print ("end")
