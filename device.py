__author__ = 'martin'
# -*- coding: utf-8 -*-

from netconfXML import netconfXML
from ncclient import manager


class Device:
    __hostname = ""
    __ipaddress = ""
    __model = ""

    def __init__(self,
                 hostname,
                 ipaddress,
                 model):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.model = model

    def pushconfig(self, config):
        print ("Applique configuration: %s - %s - %s" % (self.hostname, self.ipaddress, self.model))
        xmlstr = netconfXML.get_xml(config)
        print (xmlstr)
        m = manager.connect_ssh(self.ipaddress, port=22, username='xxxxx', password='xxxxx', device_params={'name': 'csr'})
        m.edit_config(target='running', config=xmlstr)
        m.copy_config(target='startup', source='running')

