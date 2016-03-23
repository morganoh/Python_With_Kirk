#!/usr/bin/env python

""" use paramiko to send cmd to RTR2 """



import paramiko
import time
from getpass import getpass

MAX_BUFFER = 65535

def prepare_buffer(rtr2):
    if rtr2.recv_ready():
       # print 'buffer is full'
        return rtr2.recv(MAX_BUFFER)
        
def disable_paging(rtr2):
    cmd = 'terminal length 0 \n'
    rtr2.send(cmd)
    time.sleep(1)
    prepare_buffer(rtr2)
def send_cmd(rtr2, cmd):
    #print cmd
    rtr2.send(cmd)
    time.sleep(2)
    if rtr2.recv_ready():
        return rtr2.recv(MAX_BUFFER)
    else:
        print 'buffer is empty'
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

    prepare_buffer(rtr2)
    disable_paging(rtr2)

    cmd = 'show run | inc logging \n'
    output = send_cmd(rtr2, cmd)
    print output

    cmd = 'conf t \n'
    send_cmd(rtr2, cmd)

    cmd = 'logging buffered 30000 \n'
    send_cmd(rtr2, cmd)
    
    cmd = 'exit \n'
    send_cmd(rtr2, cmd)

    cmd = 'wr \n'
    send_cmd(rtr2, cmd)

    cmd = 'show run | inc logging \n'
    output = send_cmd(rtr2, cmd)
    print output
if __name__ == "__main__":
    main() 
