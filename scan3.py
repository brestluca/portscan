from scapy.all import *

def sniff_traffic(packet):
    # Analiza los paquetes de red y detecta posibles amenazas
    if packet.haslayer(TCP):
        if packet[TCP].flags & 2: # Paquete SYN
            print(f"Se ha detectado un escaneo de puertos SYN en {packet[IP].src}!")
        elif packet[TCP].flags & 16: # Paquete ACK
            print(f"Se ha detectado un escaneo de puertos ACK en {packet[IP].src}!")
        elif packet[TCP].flags & 24: # Paquete FIN-ACK
            print(f"Se ha detectado un escaneo de puertos FIN en {packet[IP].src}!")
    elif packet.haslayer(DNS):
        if 'evil.com' in packet[DNS].qd.qname.decode('utf-8'):
            print(f"Se ha detectado una consulta DNS maliciosa a 'evil.com' desde {packet[IP].src}!")

def main():
    # Realiza una captura de tráfico en tiempo real
    sniff(prn=sniff_traffic, filter="tcp or udp or icmp or dns", store=0)

if __name__ == '__main__':
    main()
