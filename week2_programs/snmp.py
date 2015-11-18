from snmp_helper import snmp_get_oid
from snmp_helper import snmp_extract


COMMUNITY_STRING = 'galileo'
IP = '50.76.53.27'
SNMP_PORT1 = 7961
SNMP_PORT2 = 8061

OID = '1.3.6.1.2.1.1.1.0'
OID_2 = '1.3.6.1.2.1.1.5.0'


def get_sys_name(device):

    snmp_data = snmp_get_oid(device , oid = OID)
    output = snmp_extract(snmp_data)
    return output

def get_sys_description(device):
    
    snmp_data = snmp_get_oid(device , oid = OID_2)
    output = snmp_extract(snmp_data)
    return output

def main():

    first_device = (IP, COMMUNITY_STRING, SNMP_PORT1)
    second_device = (IP, COMMUNITY_STRING , SNMP_PORT2)

    sysname = get_sys_name(first_device)
    print sysname
    print '\n'

    sysdescription = get_sys_description(first_device)
    print sysdescription
    print '\n'
    
    sysname = get_sys_name(second_device)
    print sysname
    print '\n'

    sysdescription = get_sys_description(second_device)
    print sysdescription
    print '\n'


if __name__ == '__main__':
    main()
