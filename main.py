
#Importamos todas las funciones para realizar cada parte del trabajo
from libreria_funciones.leer_archivo.preguntar import(preguntar_ruta_archivo)
from libreria_funciones.leer_archivo.lectura_webs import(leer_webs_archivo)
from libreria_funciones.leer_archivo.ip_webs import (leer_ips_webs)
from libreria_funciones.mostrar_configuracion.configuración_red import (mostrar_imprimir_configuracion_red)
from libreria_funciones.comparacion_DNS.elegir_adaptador import (elegir_adaptador)
from libreria_funciones.comparacion_DNS.comparar_dns import (comparacion_dns_archivo)
from libreria_funciones.comparacion_DNS.cambiar_DNS_rapido import(cambiar_dns)
from ejecutar_permisos_administrador.lanzar_como_admin import(relanzar_como_admin)


relanzar_como_admin() #Función creada para poder ejecutar las acciones del cambio de DNS con los privilegios de adminstrador

preguntar_ruta_archivo()
input("\nPulsa Enter coninuar")

leer_webs_archivo(ruta_archivo="web.txt")
input("\nPulsa Enter coninuar")

leer_ips_webs(ruta_archivo="web.txt")
input("\nPulsa Enter coninuar")

mostrar_imprimir_configuracion_red()
input("\nPulsa Enter coninuar")

#dns_server - Lista con el DNS actual del adaptador seleccionado
#adaptador_elegido - Nombre el adaptador
dns_server, adaptador_elegido = elegir_adaptador()
input("\nPulsa Enter coninuar")

#dns_server_2 - Contenda la lista de los DNS de más rápido a menos
dns_server_2 = comparacion_dns_archivo(dns_server)
input("\nPulsa Enter coninuar")

cambiar_dns(dns_server, dns_server_2, adaptador_elegido)


input("\nPulsa Enter para cerrar...")