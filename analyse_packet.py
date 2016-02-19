

#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import base_module
import re

def my_re_of_first_line(first_line):
    m = re.match(r'(\d+.\d+)', first_line)
    if m:
        print 'ok'
        print "****group(0): \n", m.groups(0)
        #print "****group(x): \n", m.groups(1)[1:4]
    else:
        print 'failed'

def my_re_of_second_line(second_line):
    second_line = re.sub("\s+",'',second_line)
    m = re.match(r'(\d+.\d+.\d+.\d+).(\d+)>(\d+.\d+.\d+.\d+).(\w*):.*?\[(.*?)\]', second_line)
    if m:
        print 'my_re_of_second_line: ok'
        print "my_re_of_second_line: \n", m.groups(0)
        print "****group(x): \n", m.groups(1)[1:4]
        quintet = Quintet(m.groups(1)[0],m.groups(1)[1],m.groups(1)[2],m.groups(1)[3],m.groups(1)[4])
        return quintet
    else:
        print 'my_re_of_second_line: failed'

def analyse_tcpdump(file_name):
    file = open(file_name)
    i = 0
    while 1:
        line = file.readline()
        i = i+1
        if not line:
            break
        #if i > 10:
        #    break
        if i%2 != 0:
            my_re_of_first_line(line)
        else:
            my_re_of_second_line(line)


