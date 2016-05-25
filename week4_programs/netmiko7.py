#!/usr/bin/env python
'''
Use netmiko to connect to pynet-rtr1 and pynet-rtr2 and change log buffer and disable console logging
This version removes the router details and places them in a remote file(test_devices)
'''
from netmiko import ConnectHandler
from getpass import getpass
from routers import pynet1, pynet2


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
def confirm_device_buffer(rtr):
    ''' confirm the size of the switch buffer'''
    return rtr.send_command('show run | i logging buffer')
def run_remote_cmds(rtr):
    '''run commands from file (change buffer size and disable console logging)'''
    try:
        print 'cmd running ... '
        rtr.send_config_from_file(config_file = 'cmds.txt')
        print ' cmds executed '
    except:
        print 'CMDS did not execute'
def main():
    '''Set up variables amd make connection'''
    password = getpass()
    ip_addr = '50.76.53.27'
    
    routers = [pynet1, pynet2]
    
    for i in routers:
        i['password'] = password
        rtr = login(i) 
        run_remote_cmds(rtr)
        buff_size = confirm_device_buffer(rtr)
        print buff_size
if __name__ == "__main__":
    main()
