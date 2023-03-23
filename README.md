# portscan



Escaneo de puertos utilizando la biblioteca Nmap y genera un informe detallado de los resultados

Este script utiliza la biblioteca Nmap de Python para realizar un escaneo de puertos en una dirección IP específica y genera un informe detallado en formato JSON. Además, admite la opción de guardar el informe en un archivo si se proporciona una ruta.

Para ejecutar el script, simplemente debes proporcionar la dirección IP del objetivo de escaneo como argumento en la línea de comandos. Por ejemplo, para escanear los puertos en la dirección IP "192.168.1.1" y guardar el informe en un archivo llamado "report.json", puedes ejecutar el siguiente comando:

python port_scanner.py 192.168.1.1 --report report.json
