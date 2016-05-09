#!/usr/bin/env python`
'''
Use pexpect to chnage teh logging buffer size
'''

#import pexpect
from getpass import getpass
import pexpect
#import time
#import sys

def login(ssh_conn):
    """Handle the Login"""
    password = getpass()
    ssh_conn.expect('Password:')
    ssh_conn.sendline(password)
    ssh_conn.expect('pynet-rtr2#')
    print 'log in sucessful'
def confirm_logging_buffer_size(ssh_conn):
    """confirm the buffer size"""
    cmd = 'show run | i logging'
    ssh_conn.sendline(cmd)
    ssh_conn.expect('#')
    prompt = ssh_conn.before + ssh_conn.after
    return prompt.strip(cmd)
def disable_paging(ssh_conn):
    """Allow large outputs to be printed by our calls"""
    cmd = 'terminal length 0'
    ssh_conn.sendline(cmd)
    ssh_conn.expect('#')
    print 'page disable sucessful'
def enter_enable_mode(ssh_conn):
    """enter enable mode and then prove it"""
    cmd = 'conf t'
    ssh_conn.sendline(cmd)
    ssh_conn.expect('#')
    print 'now in enable mode'
def change_login_buffer_size(ssh_conn):
    """this is where we change the logging buffer size"""
    cmd = 'logging buffer 60000'
    ssh_conn.sendline(cmd)
    ssh_conn.expect('#')
    ssh_conn.sendline('end')
    ssh_conn.expect('#')
    print 'buffer size has been changed'    

def main():
    """set up connections and variables and call functions"""
    username = 'pyclass'
    ip_addr = '50.76.53.27'
    port = 8022

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    ssh_conn.timeout = 3

    login(ssh_conn)

    prompt = confirm_logging_buffer_size(ssh_conn)
    print prompt
    print '\n'
    disable_paging(ssh_conn)
    enter_enable_mode(ssh_conn)
    change_login_buffer_size(ssh_conn)
    print '\n'
    prompt = confirm_logging_buffer_size(ssh_conn)
    print prompt

    print 'Mission Sucessful'
#Things to do - remove unnessacery cmds and rtr prompts
#Smme logic to reset buffer or 
if __name__ == "__main__":
    main()























