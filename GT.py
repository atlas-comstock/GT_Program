
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import analyse_socket
import analyse_packet

#mysockets = analyse_socket.analyse_lsof("lsof.txt")
print "main program \n"
#analyse_socket.print_sockets(mysockets[1])
#analyse_socket.print_sockets(mysockets[2])
#analyse_socket.print_sockets(mysockets[4])
#analyse_socket.print_sockets(mysockets[9])
mypackets = analyse_packet.analyse_tcpdump("tcp.txt")
analyse_packet.print_packets(mypackets[1])
#analyse_packet.print_packets(mypackets[2])
#analyse_packet.print_packets(mypackets[3])
analyse_packet.print_packets(mypackets[9])
