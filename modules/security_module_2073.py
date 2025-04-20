from scapy.all import *
pkt = IP(dst='8.8.8.8')/ICMP()
sr1(pkt)
