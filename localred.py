from scapy.all import ARP, Ether, srp

# Define la dirección IP y la máscara de subred
target_ip = "192.168.1.0/24"

# Crea un paquete ARP para enviar a todos los dispositivos en la red
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp

# Envia el paquete ARP y recibe la respuesta
result = srp(packet, timeout=3, verbose=0)[0]

# Analiza la respuesta del paquete y extrae la dirección IP y la dirección MAC de cada dispositivo en la red
devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

# Imprime una lista de los dispositivos en la red
print("Devices on the network:")
print("-----------------------")
for device in devices:
    print(f"IP: {device['ip']} MAC: {device['mac']}")
