"""
import socket
import psutil
"""

import subprocess
import re

def elegir_adaptador():

    result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True, encoding='cp850')
    output = result.stdout

    dns_servers = re.findall(r'Servidores DNS.*?:\s+([\d\.]+)', output)

    if dns_servers:
        print("Servidores DNS encontrados:")
        for dns in dns_servers:
            print(f"- {dns}")
    else:
        print("No se encontraron servidores DNS.")

    """
    direccion_adaptador = psutil.net_if_addrs()
    incremental = 1

    for intf, snicaddrs in direccion_adaptador.items():
            print(f"{incremental}: {intf}\n\n")
            for snicaddr in snicaddrs:
                if snicaddr.family == psutil.AF_LINK:
                    print(f" MAC: {snicaddr.address}")
            incremental+=1
    """
