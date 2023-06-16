from scapy.all import IP, ICMP, sr1

# IP of my pc and the dest IP
ip_layer = IP(scr="192.168.178.129", dst="www.google.com")

icmp_req = ICMP()

print(icmp_req.show)

packet = ip_layer / icmp_req

received_packet: sr1(packet)

if received_packet:
    print(received_packet.show())