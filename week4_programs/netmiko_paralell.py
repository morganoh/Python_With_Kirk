#!/usr/bin/env python
'''
Use netmiko to connect to pynet-rtr1, pynet-rtr2 & juniper_srx in paralell and run 'show arp'
'''
from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet1, pynet2, juniper_srx


def login(rtr_name):
    '''make connection'''
    try:
        device_connection = ConnectHandler(**rtr_name)
        print '### YOU ARE NOW LOGGED INTO DEVICE  ###' 
        return device_connection
    except:
        print "LOGIN_FAIL"
def confirm_device(rtr):
    ''' use find prompt to confirm the device type '''
    device_type = rtr.find_prompt()
    return device_type
def run_cmd(rtr):
    ''' confirm the size of the switch buffer'''
    return rtr.send_command('show arp')
def main():
    '''Set up variables amd make connection'''
    password = getpass()
    ip_addr = '50.76.53.27'
    
    routers = [pynet1, pynet2, juniper_srx]
    
    for i in routers:
        i['password'] = password
        rtr = login(i) 
        device = confirm_device(rtr)
        print device
        output = run_cmd(rtr)
        print output
if __name__ == "__main__":
    main()
