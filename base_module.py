
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
