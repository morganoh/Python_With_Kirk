import email_helper

import pickle

from snmp_helper import snmp_extract
from snmp_helper import snmp_get_oid_v3

""" This program attempts to discover whether the configuration 
on a router in the test lab has changed between differnt runnings of the program """

IP = '50.76.53.27'
SNMP_PORT1 = 7961
SNMP_PORT2 = 8061

AUTH_KEY = 'galileo1'
ENCRYPT_KEY = 'galileo1'
A_USER = 'pysnmp'

SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'

def get_sys_name(device, user):
    ''' determine system name from MIB'''
    snmp_data = snmp_get_oid_v3(device, user, oid=SYS_NAME)
    output = snmp_extract(snmp_data)
    return output

def get_sys_uptime(device, user):
    ''' determine system uptime from MIB '''
    snmp_data = snmp_get_oid_v3(device, user, oid=SYS_UPTIME)
    output = snmp_extract(snmp_data)
    return output

def get_sys_run_change(device, user):
    ''' determine when system config last changed from MIB'''
    snmp_data = snmp_get_oid_v3(device, user, oid=RUN_LAST_CHANGED)
    output = snmp_extract(snmp_data)
    return output

def write_network_device(anylist):
    ''' write system information extarcted from MIB's into a list and save it in a file'''
    fle = open("net_dev.pk1", "wb")
    pickle.dump(anylist, fle)    
    fle.close()

def read_network_device():
    ''' This is how we extract saved system uptime from our saved file'''
    fle = open("net_dev.pk1", "rb")
    output = pickle.load(fle)
    extract_data = output[2]
    return extract_data

def make_decision(device, user):
    ''' This is where we compare current time to saved time and determine
     if it has changed , if it has we send an email'''
    
    sysuptime = get_sys_uptime(device, user)
    
    snmp_data = snmp_get_oid_v3(device, user, oid=RUN_LAST_CHANGED)
    #current_run_variable = snmp_extract(snmp_data)
    prev_run_variable = read_network_device()

    if sysuptime  > prev_run_variable:
        send_email()
        print 'router config has changed , email sent'
    else:
        print 'no change in the config of device under test'

    return sysuptime

def send_email():
    ''' this is how we send email '''
    sender = 'morganoh@twb-tech.com'
    recipient = 'mohalloran@salesforce.com'
    subject = 'Router Config Has Changed'
    message = 'the device you are testing has registered a config change'
    
    email_helper.send_mail(recipient, subject, message, sender)
    
def main():
    ''' main function - run steh programs from global variables and defined methods '''
    snmp_user = (A_USER, AUTH_KEY, ENCRYPT_KEY)
    first_device = (IP, SNMP_PORT1)
    second_device = (IP, SNMP_PORT2)

    print '\n'
    sysname = get_sys_name(second_device, snmp_user)
    print 'Sytem Name is %s' % sysname
    print '\n'
    

    sysuptime = get_sys_uptime(second_device, snmp_user)
    #print 'System uptime is %s ' % sysuptime
    #print '\n'

    sysrun = get_sys_run_change(second_device, snmp_user)
    print 'Time since last change of running config %s' % sysrun
    print '\n'

    network_parameters_list = [sysname, sysuptime, sysrun]

    write_network_device(network_parameters_list)

    saved_device_parameters = read_network_device()
    print '\n'
    print 'Time since running config last changed from file is : %s' % saved_device_parameters
    
    second_run = make_decision(second_device, snmp_user)
    print '\n'
    print 'Time since running config changed from current run is  %s' % second_run



if __name__ == '__main__':
    main()




