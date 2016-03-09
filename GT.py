
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import analyse_socket
import analyse_packet

class Discriminators(object):
    def __init__(self, num_of_forward_message, num_of_backward_message,
                 size_of_forward_message, size_of_backward_message,
                 min_len_of_forward_message, min_len_of_backward_message,
                 avg_len_of_forward_message, avg_len_of_backward_message,
                 stand_deviation_len_of_forward_message, stand_deviation_of_backward_message,
                 min_arrive_timegap_of_forward_message, min_arrive_timegap_of_backward_message,
                 avg_arrive_timegap_of_forward_message, avg_arrive_timegap_of_backward_message,
                 max_arrive_timegap_of_forward_message, max_arrive_timegap_of_backward_message,
                 stand_deviation_arrive_timegap_of_forward_message, stand_deviation_arrive_timegap_of_backward_message,
                 num_of_urgent_forward_message, num_of_urgent_backward_message,
                 num_of_push_forward_message, num_of_push_backward_message,
                 time_duration_of_stream):
        pass

#mysockets = analyse_socket.analyse_lsof("lsof.txt")
print "main program \n"
#analyse_socket.print_sockets(mysockets[1])
#analyse_socket.print_sockets(mysockets[2])
#analyse_socket.print_sockets(mysockets[4])
#analyse_socket.print_sockets(mysockets[9])
mypackets = analyse_packet.analyse_tcpdump("new.txt")
analyse_packet.print_packets(mypackets[1])
#analyse_packet.print_packets(mypackets[2])
#analyse_packet.print_packets(mypackets[3])
analyse_packet.print_packets(mypackets[9])

