# portscan

Es importante destacar que este script solo debe utilizarse con fines educativos y en entornos controlados. La realización de escaneos de red sin permiso es ilegal y puede causar daños significativos a los sistemas informáticos y la red.


Escaneo de puertos utilizando la biblioteca Nmap y genera un informe detallado de los resultados

Este script utiliza la biblioteca Nmap de Python para realizar un escaneo de puertos en una dirección IP específica y genera un informe detallado en formato JSON. Además, admite la opción de guardar el informe en un archivo si se proporciona una ruta.

Para ejecutar el script, simplemente debes proporcionar la dirección IP del objetivo de escaneo como argumento en la línea de comandos. Por ejemplo, para escanear los puertos en la dirección IP "192.168.1.1" y guardar el informe en un archivo llamado "report.json", puedes ejecutar el siguiente comando:

python port_scanner.py 192.168.1.1 --report report.json



# scan2

Este script utiliza la biblioteca Scapy de Python para realizar un escaneo de red básico y detectar hosts activos en una red. A continuación, escanea los puertos en cada host activo y enumera los puertos abiertos en cada host.


# scan3

Este script utiliza la biblioteca Scapy de Python para realizar una captura de tráfico de red en tiempo real y analizar los paquetes para detectar posibles amenazas. En este ejemplo, el script detecta escaneos de puertos SYN, ACK y FIN, así como consultas DNS maliciosas a un dominio malicioso específico.
