
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import analyse_socket
import analyse_packet

mysockets = analyse_socket.analyse_lsof("lsof.txt")
print "main program \n"
mysockets
print mysockets[1].process_command_name
print mysockets[1].Quintet.Stat
analyse_socket.print_sockets(mysockets[1])
#print mysockets[1].process_command_name
#print mysockets[0].time_stamp
print mysockets[1].time_stamp
#analyse_packet.analyse_tcpdump("tcp.txt")
