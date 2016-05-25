#!/usr/bin/env python
'''
Use netmiko to connect to pynet-rtr1 and pynet-rtr2 and change log buffer and disable console logging
'''
from netmiko import ConnectHandler
from getpass import getpass

def login(rtr_name):
    '''make connection'''
    print rtr_name
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
    pynet1 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'22', 
    }
    pynet2 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'8022',
    }
    
    
    routers = [pynet1, pynet2]
    
    for i in routers:
        rtr = login(i)

        device = confirm_device(rtr)
        print 'You have logged sucessfuly into %s' % device
        
        pre_buff_size = confirm_device_buffer(rtr)
        print pre_buff_size
        run_remote_cmds(rtr)
        post_buff_size = confirm_device_buffer(rtr)
        print post_buff_size  
if __name__ == "__main__":
    main()
