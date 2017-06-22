#!/usr/bin/env python 

class NetDev(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.vend = ""
        print(self.ip_addr)
        print(self.username)
        print(self.password)
        
    def prints_ip(self):
        print(self.ip_addr)

    def vend_update(self, vend):
        self.vend=vend
        print(self.vend)
        
    def dev_print(self):
        print(self.vend)
        print(self.ip_addr)
        print(self.username)
        print(self.password)


dev1 = NetDev(ip_addr = "10.1.4.3", username ="baudet", password="immp")
dev2 = NetDev(ip_addr = "10.1.4.4", username ="baudet", password="immp")
dev3 = NetDev(ip_addr = "10.1.4.5", username ="baudet", password="immp")
dev4 = NetDev(ip_addr = "10.1.4.6", username ="baudet", password="immp")

dev1.prints_ip()
dev2.prints_ip()

dev1.vend_update(vend="Cisco")
dev1.dev_print()
dev2.dev_print()

#ip_addr, username, password, serial_number, model, vendor, uptime, os_version