#!/usr/bin/env python
'''
Use netmiko to connect to RTR2 and enter config mode - then verify this 
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
def enter_config_mode(rtr2):
    rtr2.config_mode()
    return rtr2.find_prompt()
def main():
    """set up variables and call functions"""
    password = getpass()
    pynet2 = {
        'device_type':'cisco_ios', 'ip':'50.76.53.27', 'username':'pyclass', 'password':password, 'port':'8022',
    }
    rtr2 = login(pynet2)
    goal = enter_config_mode(rtr2)
    print 'The returned prompt is: %s' %goal
if __name__ == "__main__":
    main()
