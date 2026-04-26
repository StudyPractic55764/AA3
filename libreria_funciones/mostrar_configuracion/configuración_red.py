import psutil
import socket

def mostrar_imprimir_configuracion_red():
    
    print("-"*40)
    print("LISTAR E IMPRIMIR CONFIGURACIONES DE RED")
    print("-"*40)

    #Mostramos las direcciones de todos los adaptadores con sus respectivos estados
    direccion_adaptador = psutil.net_if_addrs()
    estados_adaptador = psutil.net_if_stats()

    #Crear una variable para guardar una cadena con todo el informe para luego imprimirlo en pantalla y en el documento.
    informe = "---INFORME DE CONFIGURACION DE RED---\n"

    #Recorremos cada adaptador de red disponible
    for intf, addr_list in direccion_adaptador.items():
        informe += f"~~~~Adaptador: {intf}~~~~\n\n"

        #Verificamos que el adaptador tiene informacion sobre el estado
        if intf in estados_adaptador:
            estado = estados_adaptador[intf]
            #isup indica si el adaptador esta operativo
            informe += f"Estado: {'[Activo]' if estado.isup else '[Inactivo]'}\n"
            informe += f"Velocidad: {estado.speed}Mb\n"

        #Recorremos todas las direcciones del adaptador actual
        for direccion_adaptador in addr_list:
            if direccion_adaptador.family == socket.AF_INET:
                informe += f" IP IPv4: {direccion_adaptador.address}\n"
                informe += f" Mascara: {direccion_adaptador.netmask}\n"
                informe += f"Broadcast: {direccion_adaptador.broadcast}\n"
            elif direccion_adaptador == socket.AF_INET6:
                informe += f" IP IPv6: {direccion_adaptador.address}\n"
            elif hasattr(psutil, 'AF_LINK') and direccion_adaptador.family == psutil.AF_LINK:
                informe += f"MAC: {direccion_adaptador.address}\n"
        informe += "-"*40+"-\n\n"

    #Mostramos por pantalla el resultado  
    print(informe)

    #Escribir todo el informe dentro del archivo de texto "configuracion_local.txt"
    with open("configuracion_local.txt", "w", encoding="utf-8") as archivo:
        archivo.write(informe)

    print("El informe se ha guardado correctamente en el archivo 'configuracion_local.txt'\n")
          
    