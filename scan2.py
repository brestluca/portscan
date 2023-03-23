from scapy.all import *

def scan_network(ip_range):
    # Escanea la red especificada para detectar hosts activos y devuelve una lista de direcciones IP
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=False)
    hosts = []
    for pair in ans:
        hosts.append(pair[1].psrc)
    return hosts

def scan_ports(host):
    # Escanea los puertos en el host especificado y devuelve una lista de puertos abiertos
    ports = []
    for port in range(1, 1001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            ports.append(port)
        sock.close()
    return ports

def main():
    # Escanea la red local para detectar hosts activos
    ip_range = '192.168.0.1/24'
    hosts = scan_network(ip_range)
    print(f"Se han encontrado los siguientes hosts activos en la red: {hosts}")

    # Escanea los puertos en cada host y enumera los puertos abiertos
    for host in hosts:
        ports = scan_ports(host)
        if ports:
            print(f"Se han encontrado los siguientes puertos abiertos en {host}: {ports}")
        else:
            print(f"No se han encontrado puertos abiertos en {host}")

if __name__ == '__main__':
    main()
