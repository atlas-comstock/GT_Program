

#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import base_module
import re

class Packet(object):
    def __init__(self, packet_length, protocol_name, Quintet, flag, time_stamp):
        pass
        self.packet_length = packet_length
        self.protocol_name = protocol_name
        self.Quintet = Quintet
        self.flag = flag
        self.time_stamp = time_stamp

def my_re_of_first_line(first_line, packet):
    m = re.match(r'(\w+.\w+)(.*)proto\s(.*)length\s(\d+)\)', first_line)
    if m:
        print 'my_re_of_first_line: ok'
        print "my_re_of_first_line: \n", m.groups(0)
        packet.time_stamp = m.groups(1)[0]
        packet.protocol_name = m.groups(1)[2]
        packet.packet_length = m.groups(1)[3]
#        print "group(x): \n", m.groups(1)[0]
#        print "group(x): \n", m.groups(1)[1]
#        print "group(x): \n", m.groups(1)[2]
#        print "group(x): \n", m.groups(1)[3]
    else:
        print 'my_re_of_first_line: failed'

def my_re_of_second_line(second_line, packet):
    second_line = re.sub("\s+",'',second_line)
    m = re.match(r'(\w+.\w+.\w+.\w+).(\w+)>(\w+.\w+.\w+.\w+).(\w*):.*?\[(.*?)\]', second_line)
    if m:
        print 'my_re_of_second_line: ok'
        print "my_re_of_second_line: \n", m.groups(0)
        print "****group(x): \n", m.groups(1)[1:4]
        quintet = base_module.Quintet(m.groups(1)[0],m.groups(1)[1],m.groups(1)[2],m.groups(1)[3],m.groups(1)[4])
        packet.quintet = quintet
        packet.flag = m.groups(1)[4]
    else:
        print 'my_re_of_second_line: failed************\n\n'
        print second_line

def analyse_tcpdump(file_name):
    file = open(file_name)
    i = 0
    packet = Packet
    all_packets = [Packet]
    while 1:
        line = file.readline()
        i = i+1
        if not line:
            break
        if i > 30:
            break
        if i%2 != 0:
            my_re_of_first_line(line, packet)
        else:
            my_re_of_second_line(line, packet)
            all_packets.append(packet)
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
    print "time_stamp ", mypackets.time_stamp
