from scapy.all import Ether, ARP, srp, conf
import sys
import time


def arp_scan(iface, ip_range):
    print("[+] Scanning ", ip_range)
    curr_time = time.time()
    print("[+] Scan started at ", time.ctime(curr_time))
    conf.verb = 0
    broadcast = "ff:ff:ff:ff:ff:ff"
    ether_layer = Ether(dst=broadcast) 
    arp_layer = ARP(pdst=ip_range)

    packet = ether_layer/arp_layer

    ans, unans = srp(packet, iface=iface, timeout=2, inter=0.1)

    for snd, rcv in ans:
        ip = rcv[ARP].psrc
        mac = rcv[Ether].src 
        print(ip, mac)
    duration = time.time() - curr_time
    print("[+] Scan completed, Duration: ", duration)
# scanner.py eth0 192.168.0.1/24
if __name__ == "__main__":
    iface = sys.argv[1]
    ip_range = sys.argv[2]
    arp_scan(iface, ip_range)


