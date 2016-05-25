#!/usr/bin/env python
'''
Use netmiko to connect to 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
'''
from netmiko import ConnectHandler
from getpass import getpass

def login(rtr_name):
    '''make connection'''
    try:
        device_connection = ConnectHandler(**rtr_name)
        print '### YOU ARE NOW LOGGED INTO DEVICE ###'
        print rtr_name['device_type']
        return device_connection
    except:
        print "LOGIN_FAIL"
def run_cmd(rtr):
    '''run command show arp on all devices '''
    return rtr.send_command('show arp')
    
def main():
    '''Set up variables amd make connection'''
    password = getpass()

    pynet1 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'22',
    }
    pynet2 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'8022',  
    }
    
    juniper_srx = {
        'device_type':'juniper', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'9822',
    }
    
    routers = [pynet1, pynet2, juniper_srx]
    
    for i in routers:
        rtr = login(i)
        output = run_cmd(rtr)
        print output
if __name__ == "__main__":
    main()
