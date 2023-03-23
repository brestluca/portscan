#!/usr/bin/env python
import nmap
import argparse
import json
from datetime import datetime

def nmap_scan(target):
    # Realiza un escaneo de puertos en la dirección IP especificada utilizando Nmap
    nm = nmap.PortScanner()
    nm.scan(target)
    return nm

def generate_report(target, nm):
    # Genera un informe de escaneo detallado en formato JSON
    report = {
        "target": target,
        "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scan_results": nm[target]
    }
    return json.dumps(report, indent=4)

def main():
    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Realiza un escaneo de puertos en una dirección IP utilizando Nmap')
    parser.add_argument('target', metavar='target', type=str, help='La dirección IP del objetivo de escaneo')
    parser.add_argument('--report', metavar='report', type=str, help='La ruta del archivo de informe de escaneo')
    args = parser.parse_args()

    # Realiza el escaneo de puertos utilizando Nmap
    nm = nmap_scan(args.target)

    # Genera el informe de escaneo detallado en formato JSON
    report = generate_report(args.target, nm)

    # Guarda el informe de escaneo en un archivo si se proporciona una ruta
    if args.report:
        with open(args.report, 'w') as report_file:
            report_file.write(report)

    # Imprime el informe de escaneo en la consola
    print(report)

if __name__ == '__main__':
    main()
