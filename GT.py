
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import analyse_socket
import analyse_packet

analyse_socket.analyse_lsof("lsof.txt")
analyse_packet.analyse_tcpdump("tcp.txt")
