__author__ = 'martin'

import xml.etree.ElementTree
import string


class netconfXML:

    @staticmethod
    def get_xml(configtable):

        root = xml.etree.ElementTree.Element('config')

        cli_config_data = xml.etree.ElementTree.SubElement(root, 'cli-config-data')

        for line in configtable:
            if line != '' and line != '!':
                cmd = xml.etree.ElementTree.SubElement(cli_config_data, 'cmd')
                cmd.text = line

        return xml.etree.ElementTree.tostring(root, encoding='utf8', method='xml')
