__author__ = 'martin'

from device import Device


class DeviceList:
    __devices = []

    def __init__(self, devicerawtable):
        for devitem in devicerawtable:
            self.__devices.append(
                Device(devitem['hostname'],
                       devitem['ipaddress'],
                       devitem['model']))

    def pushconfig(self, configlines):
        for devitem in self.__devices:
            devitem.pushconfig(configlines)
