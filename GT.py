
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
analyse_packet.print_packets(mypackets[2])
analyse_packet.print_packets(mypackets[3])
analyse_packet.print_packets(mypackets[9])
analyse_packet.print_packets(mypackets[19])
analyse_packet.print_packets(mypackets[29])
analyse_packet.print_packets(mypackets[49])

num_of_forward_message = 0
num_of_backward_message = 0
unknow = 0
list_length = []
for single_packet in mypackets:
    #print single_packet.packet_length
    list_length.append(single_packet.packet_length)
    if single_packet.is_forward_message == 1:
        num_of_forward_message = num_of_forward_message+1
        print "forward ", single_packet.quintet.SrcIp, single_packet.quintet.SrcPort
        print "backward ", single_packet.quintet.DstIP, single_packet.quintet.DstPort, "\n"
    elif single_packet.is_forward_message == 0:
        num_of_backward_message = num_of_backward_message+1
        print "forward ", single_packet.quintet.SrcIp, single_packet.quintet.SrcPort, "\n"
        print "backward ", single_packet.quintet.DstIP, single_packet.quintet.DstPort
    else:
        unknow = unknow + 1

print "\n\n\nnum_of_forward_message is ", num_of_forward_message
print "\nnum_of_backward_message is ", num_of_backward_message
print "unknow  is ", unknow

# Convert all strings in a list to int
list_length = [int(i) for i in list_length]
print min(list_length)
print max(list_length)
#print mypackets.packet_length.index(min(mypackets.packet_length))
