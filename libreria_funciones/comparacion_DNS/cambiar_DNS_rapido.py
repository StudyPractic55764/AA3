import subprocess


def cambiar_dns(dns_server, resultado, adaptador_elegido):
    print("-"*40)
    print(f"ACTUALIZANDO DNS...")
    print("-"*40)

    #Extraemos la DNS actual del adaptador que elegimos anteriormente
    dns_principal = dns_server[0]

    #Extraemos la DNS más rapida de la lista ordenada
    dns_mas_rapida = resultado[0]['DNS']

        #Comparamos las dos DNS
    if dns_principal == dns_mas_rapida:
        print(f"El DNS de tu adaptador es el más rapido de la lista")
        return dns_principal
    else:
        try:
            cmd = [
                #Comando para ejecutar la configuracion de DNS
                'netsh', 'interface', 'ipv4', 'set', 'dnsservers',
                f"name={adaptador_elegido}",
                "static", #Configuración manual y no DHCP
                dns_mas_rapida,
                "primary",  #DNS primario
                "validate=no" #No validar el servidor DNS
            ]

            #Ejecutamos el comando en el sistema
            subprocess.run(cmd, capture_output=True, text=True, check=True)

            #Limpiamos la caché DNS del sistema para que se efectuen los cambios que queremos realizar
            subprocess.run(['ipconfig', '/flushdns'], capture_output=True)

            print(f"DNS cambiado a: {dns_mas_rapida}")
            return dns_mas_rapida

        except Exception as e:
            print(f"Error al cambiar DNS: {e}")
            return None
    

    
    


