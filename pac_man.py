from scapy.all import IP, ICMP, sr1

ip_layer = IP(scr="192.168.0.40", dst="www.google.com")

icmp_req = ICMP