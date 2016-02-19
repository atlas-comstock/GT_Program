import re
class Quintet(object):
    def __init__(self, SrcIp, SrcPort, DstIP, DstPort, Stat):
        self.SrcIp = SrcIp
        self.SrcPort = SrcPort
        self.DstIP = DstIP
        self.DstPort = DstPort
        self.Stat = Stat

def my_re(input_to_analyse):
    print "****input_to_analyse: \n", input_to_analyse
    m = re.match(r'(.*):(.*)::(.*):(.*?)@(.*)', input_to_analyse)
    if m:
        print 'ok'
       # print "****group(0): \n", m.groups(0)
       # print "****group(x): \n", m.groups(1)[0:4]
        quintet = Quintet(m.groups(1)[0],m.groups(1)[1],
m.groups(1)[2],m.groups(1)[3],m.groups(1)[4])
    else:
        print 'failed'

file = open("input.txt")
i = 0
while 1:
    if i > 10:
        break
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
        my_re(Internet_address)
    elif line[0] == 'f':
        status = line[1:]
        print "status ", status
    else:
        time_stamp = line
        print "time_stamp ", time_stamp
