
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import base_module
import re

def my_re(Internet_address):
    #print "****input_to_analyse: \n", Internet_address
    m = re.match(r'(.*):(.*)::(.*):(.*?)@(.*)', Internet_address)
    if m:
        #print 'ok'
        #print "****group(0): \n", m.groups(0)
        #print "****group(x): \n", m.groups(1)[1:4]
        quintet = base_module.Quintet(m.groups(1)[0],m.groups(1)[1],m.groups(1)[2],m.groups(1)[3],m.groups(1)[4])
        return quintet
    else:
        print 'failed'

def analyse_lsof(file_name):
    file = open(file_name)
    i = 0
    while 1:
        #    if i > 10:
        #        break
        i = i+1
        line = file.readline()
        if not line:
            break
        if line[0] == 'c':
            process_command_name = line[1:]
            print "process_command_name ", process_command_name
        elif line[0] == 't':
            IP_type = line[1:]
            print "IP_type ", IP_type
        elif line[0] == 'p':
            process_ID = line[1:]
            print "process_ID ", process_ID
        elif line[0] == 'P':
            protocol_name = line[1:]
            print "protocol_name ", protocol_name
        elif line[0] == 'n':
            Internet_address = line[1:]
            print "Internet_address ", Internet_address
            quintet = my_re(Internet_address)
            print "quintet.Stat ", quintet.Stat
        elif line[0] == 'f':
            status = line[1:]
            print "status ", status
        else:
            time_stamp = line
            print "time_stamp ", time_stamp

