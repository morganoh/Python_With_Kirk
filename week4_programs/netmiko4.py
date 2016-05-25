#!/usr/bin/env python
'''
Use netmiko to connect to RTR2 and change buffer size
**NOTE:** need some kind of buffer logic that will make the change and flip based on the size on the size it reads
'''
from netmiko import ConnectHandler
from getpass import getpass

def login(pynet2):
    """make connection"""
    try:
        pynet_rtr2 = ConnectHandler(**pynet2)
        return pynet_rtr2
    except:
        print "LOGIN FAIL"
def confirm_buffer_size(rtr2):
    '''confirm size of the switch buffer'''
    return rtr2.send_command('show run | include logging buffer')

def change_buffer(rtr2):
    ''' change the size of the buffer '''
    config_cmds = ['logging buffered 65000']
    rtr2.send_config_set(config_cmds)
    changed = confirm_buffer_size(rtr2)
    return changed
def main():
    """set up variables and call functions"""
    password = getpass()
    pynet2 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'8022',
    }
    rtr2 = login(pynet2)
    buff_size = confirm_buffer_size(rtr2)
    print buff_size
    buff = change_buffer(rtr2)
    print buff
    
if __name__ == "__main__":
    main()
