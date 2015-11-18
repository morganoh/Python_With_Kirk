#!/usr/bin/env python

import telnetlib
import time
import sys
import socket

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_cmd(remote_conn, cmd):
    cmd.rstrip('\n')
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def login(remote_conn,username, password):
    output =   remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def make_connection(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit(" Connection Timed Out !!")

def process_output(some_input):
    sliced_output = some_input[17:707]
    return sliced_output

def main():
    username = 'pyclass'
    password = '88newclass'
    ip_addr = '50.76.53.27'


    remote_conn = make_connection(ip_addr)
    
    output = login(remote_conn, username, password)

    time.sleep(1)
    output = remote_conn.read_very_eager()

    output = send_cmd(remote_conn, 'terminal length 0')
    ver_output = send_cmd(remote_conn, 'show version') 

    ip_output = send_cmd(remote_conn, 'show ip int brief')   
    
    processed_output = process_output(ip_output)
    print processed_output




    remote_conn.close()


# what about classes ? passing objects/variables into functions repeatedly => use classes

# now we should also thinkn about processing ak this output with a function

if __name__ == "__main__":
        main()



