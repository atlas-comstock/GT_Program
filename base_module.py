
#!/usr/bin/env python
# -*- coding: utf-8 -*-
' a base module '

__author__ = 'YongHao Hu'

class Quintet(object):
    def __init__(self, SrcIp, SrcPort, DstIP, DstPort, Stat):
        self.SrcIp = SrcIp
        self.SrcPort = SrcPort
        self.DstIP = DstIP
        self.DstPort = DstPort
        self.Stat = Stat

class Socket(object):
    def __init__(self, process_command_name, IP_type, process_ID, protocol_name, Quintet, time_stamp):
        self.process_command_name = process_command_name
        self.IP_type = IP_type
        self.process_ID = process_ID
        self.protocol_name = protocol_name
        self.Quintet = Quintet
        self.time_stamp = time_stamp
