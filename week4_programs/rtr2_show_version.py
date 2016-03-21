#!/usr/bin/env python

""" use paramiko to sne cmd to RTR2 """



import paramiko
import time
from getpass import getpass

MAX_BUFFER = 65535

def check_buffer_is_ready(rtr2, cmd):
    """
    if buffer is true - print , else send cmd
    """
    if  rtr2.recv_ready():
        print 'buffer is ready'
        output = rtr2.recv(MAX_BUFFER)
        print output
    else:
        send_command(rtr2, cmd)
    
def send_command(rtr2, cmd):
    """
    take the cmd and print output
    """
    rtr2.send(cmd)
    time.sleep(1)
    output = rtr2.recv(MAX_BUFFER)
    print output
#def disable_paging():

def main():
    """
    set up paramiko cxn and send the cmd
    """
    ip_addr = '50.76.53.27'
    port = 8022
    username = 'pyclass'
    password = getpass()
    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.load_system_host_keys()
    remote_conn_pre.connect(ip_addr, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    rtr2 = remote_conn_pre.invoke_shell()
    cmd = 'terminal length 0 \n'
    check_buffer_is_ready(rtr2, cmd)
    cmd = 'show ip int br \n'
    check_buffer_is_ready(rtr2, cmd)
    cmd = 'show version \n'
    check_buffer_is_ready(rtr2, cmd)
if __name__ == "__main__":
    main() 
