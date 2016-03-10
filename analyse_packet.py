

#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import base_module
import re
import string

class Packet(object):
    def __init__(self, packet_length, protocol_name, Quintet, flag, time_stamp, is_forward_message):
        pass
        self.packet_length = packet_length
        self.protocol_name = protocol_name
        self.Quintet = Quintet
        self.flag = flag
        self.time_stamp = time_stamp
        self.is_forward_message = is_forward_message

def my_re_of_second_line(second_line, packet):
    second_line = re.sub("\s+",'',second_line)
    m = re.match(r'(\w+.\w+.\w+.\w+).(\w+)>(\w+.\w+.\w+.\w+).(.*):Flags\[(.*?)\]', second_line)
    if m:
        print 'my_re_of_second_line: ok'
        print "my_re_of_second_line: \n", m.groups(0)
        print "****group(x): \n", m.groups(1)[1:4]
        quintet = base_module.Quintet(m.groups(1)[0],m.groups(1)[1],m.groups(1)[2],m.groups(1)[3],m.groups(1)[4])
        packet.quintet = quintet
        packet.flag = m.groups(1)[4]
        m = re.match(r'(\w+).(\w+).(\w+).(\w+)', quintet.SrcIp)
        if m:
            a = string.atoi(m.groups(1)[0])
            b = string.atoi(m.groups(1)[1])
            c = string.atoi(m.groups(1)[2])
            d = string.atoi(m.groups(1)[3])
            #local ip or remote ip
            if a==10 & b>=0 & b<=255 & c>=0 & c<=255 & d>=0 & d<=255:
                packet.is_forward_message = 1
            elif a==172 & b>=16 & b<=31 & c>=0 & c<=255 & d>=0 & d<=255:
                packet.is_forward_message = 1
            elif a==192 & b==168 & c>=0 & c<=255 & d>=0 & d<=255:
                packet.is_forward_message = 1
            else:
                packet.is_forward_message = 0
        else:
            packet.is_forward_message = -1
            print "quintet.SrcIp "
            print quintet.SrcIp
        return 1
    else:
        print 'my_re_of_second_line: failed************\n\n'
        print second_line
        return 0


def my_re_of_first_line(first_line, packet):
    m = re.match(r'(\w+.\w+)(.*)proto\s(.*)length\s(\d+)\)', first_line)
    if m:
        print 'my_re_of_first_line: ok'
        print "my_re_of_first_line: \n", m.groups(0)
        packet.time_stamp = m.groups(1)[0]
        packet.protocol_name = m.groups(1)[2]
        packet.packet_length = m.groups(1)[3]
        return 0
#        print "group(x): \n", m.groups(1)[0]
#        print "group(x): \n", m.groups(1)[1]
#        print "group(x): \n", m.groups(1)[2]
#        print "group(x): \n", m.groups(1)[3]
    else:
        print first_line
        if my_re_of_second_line(first_line, packet):
            return 1
        else:
            print 'my_re_of1,2: failed'
            return 0

packet = Packet
def analyse_tcpdump(file_name):
    file = open(file_name)
    i = 0
    all_packets = [Packet]
    while 1:
        line = file.readline()
        i = i+1
        if not line:
            break
#        if i > 30:
#            break
        if my_re_of_first_line(line, packet):
            all_packets.append(Packet(packet.packet_length, packet.protocol_name, packet.quintet, packet.flag, packet.time_stamp, packet.is_forward_message))
            print "print packe"
            print_packets(packet)
    print "final"
    print_packets(all_packets[1])
    print_packets(all_packets[2])
    print_packets(all_packets[3])
    print_packets(all_packets[9])
    print_packets(all_packets[19])
    return all_packets

def print_Quintet(quintet):
    print "SrcIp ", quintet.SrcIp
    print "SrcPort ", quintet.SrcPort
    print "DstIP ", quintet.DstIP
    print "DstPort ", quintet.DstPort
    print "Stat ", quintet.Stat

def print_packets(mypackets):
    print "packet_length ", mypackets.packet_length
    print "protocol_name ", mypackets.protocol_name
    print_Quintet(mypackets.quintet)
    print "flag ", mypackets.flag
    print "time_stamp ", mypackets.time_stamp, "\n\n"
