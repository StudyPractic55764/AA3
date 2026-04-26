
import subprocess
import re

def cambiar_dns(dns_server, resultado, adaptador_elegido):
    dns_principal = dns_server[0]
    dns_mas_rapida = resultado[0]['DNS']
    if dns_principal == dns_mas_rapida:
        print(f"El DNS de tu adaptador es el más rapido de la lista")
        return dns_principal
    else:
        try:
            cmd = [
                'netsh', 'interface', 'ipv4', 'set', 'dnsservers',
                f"name={adaptador_elegido}",
                "static",
                dns_mas_rapida,
                "primary",
                "validate=no"
            ]
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            subprocess.run(['ipconfig', '/flushdns'], capture_output=True)

            print(f"DNS cambiado a: {dns_mas_rapida}")
            return dns_mas_rapida

        except Exception as e:
            print(f"Error al cambiar DNS: {e}")
            return None
    

    
    


