from scapy.all import srp, conf
from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP
import sys
import time


def arp_scan(iface, ip_range): 
    print("[+] Scanning ", ip_range)   # print IP range being scanned
    curr_time = time.time()
    print ("[+] Scan started at ", time.ctime(curr_time)) # print time in readable form
    conf.verb = 0                      # set verbose level to 0
    broadcast = "ff:ff:ff:ff:ff:ff"    # broadcast mac address 
    ether_layer = Ether(dst=broadcast) # ethernet layer with broadcast mac address
    arp_layer = ARP(pdst=ip_range)

    packet = ether_layer / arp_layer

    # send packet on the specified network interface
    ans, unans = srp(packet, iface=iface, timeout=2, inter=0.1)

    # print IP and the mac adress 
    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac =rcv[Ether].src
        print(ip, mac)

    duration = time.time() - curr_time
    print("[+] Scan completed, Duration: ", duration)


# This code retrives the command line arguments
# scanner.py eth0 <IP-range> ex:172.16.1.0/24
if __name__ == "__main__":
    iface =sys.argv[1]
    ip_range = sys.argv[2]
    arp_scan(iface, ip_range)


# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python scanner.py <interface> <IP range>")
#         sys.exit(1)

#     iface = sys.argv[1]
#     ip_range = sys.argv[2]
#     arp_scan(iface, ip_range)
