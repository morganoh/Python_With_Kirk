#!/usr/bin/env/ python

'''
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
'''
import pexpect
from getpass import getpass
import time

def login(ssh_conn):
    """Handle the Login"""
    try:
        password = getpass()
        ssh_conn.expect('Password:')
        ssh_conn.sendline(password)
        ssh_conn.expect('pynet-rtr2#')     
    except:
        print 'REACHED TIMEOUT, LOGIN UNSUCESSFUL'

def handle_output(ssh_conn, cmd):
    """Handle the outpout of anything we decide to do"""
    ssh_conn.sendline(cmd)
    ssh_conn.expect('pynet-rtr2#')
    prompt = ssh_conn.before
    return prompt.strip(cmd)

def main():
    username = 'pyclass'
    ip_addr = '50.76.53.27'
    port = 8022

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3

    login(ssh_conn)
    time.sleep(1)
    cmd = ('show ip int br')
    returned_cmd = handle_output(ssh_conn, cmd)
    print returned_cmd
if __name__ == "__main__":
    main()
