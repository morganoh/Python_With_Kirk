''' This program attempts to discover whether the configuration
on a router in the test lab has changed between differnt runnings of the program
'''


import time
import line_graph
from snmp_helper import snmp_extract
from snmp_helper import snmp_get_oid_v3


IP = '50.76.53.27'
SNMP_PORT1 = 7961
SNMP_PORT2 = 8061

AUTH_KEY = 'galileo1'
ENCRYPT_KEY = 'galileo1'
A_USER = 'pysnmp'

snmp_oids = ['1.3.6.1.2.1.2.2.1.10.5', '1.3.6.1.2.1.2.2.1.11.5', '1.3.6.1.2.1.2.2.1.16.5', '1.3.6.1.2.1.2.2.1.17.5']

def get_packet_stats(device, user, oid):
    '''extract packet counts using the mibs '''
    snmp_data = snmp_get_oid_v3(device, user, oid)
    output = snmp_extract(snmp_data)
    return int(output)
def main():
    ''' main function - runs the programs from global variables and defined methods '''
    snmp_user = (A_USER, AUTH_KEY, ENCRYPT_KEY)
    pynet_rtr2 = (IP, SNMP_PORT2)

    in_packet_list = []
    out_packet_list = []
    in_packet_unicast_list = []
    out_packet_unicast_list = []


    print '\n'

    for time_track in range(0, 65, 5):

        print "\n%20s %-60s" % ("time", time_track)
        in_packet_list.append(get_packet_stats(pynet_rtr2, snmp_user, snmp_oids[0]))
        out_packet_list.append(get_packet_stats(pynet_rtr2, snmp_user, snmp_oids[1]))
        in_packet_unicast_list.append(get_packet_stats(pynet_rtr2, snmp_user, snmp_oids[2]))
        out_packet_unicast_list.append(get_packet_stats(pynet_rtr2, snmp_user, snmp_oids[3]))
        
    time.sleep(300)

    
    x_labels = []
    for x_label in range(5, 65, 5):
        x_labels.append(str(x_label))


      # Create the graphs
    if line_graph.twoline("pynet-rtr2-octets.svg", "pynet-rtr2 Fa4 Input/Output Bytes",
                          in_packet_list, "In Octets", out_packet_list,
                          "Out Octets", x_labels):
        print "In/Out Octets graph created"

    if line_graph.twoline("pynet-rtr2-pkts.svg", "pynet-rtr2 Fa4 Input/Output Unicast Packets",
                          in_packet_unicast_list, "In Packets", out_packet_unicast_list,
                          "Out Packets", x_labels):
        print "In/Out Packets graph created"

                    
if __name__ == '__main__':
    main()




