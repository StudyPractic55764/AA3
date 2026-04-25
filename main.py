from libreria_funciones.leer_archivo.preguntar import(preguntar_ruta_archivo)
from libreria_funciones.leer_archivo.lectura_webs import(leer_webs_archivo)
from libreria_funciones.leer_archivo.ip_webs import (leer_ips_webs)
from libreria_funciones.mostrar_configuracion.configuración_red import (mostrar_imprimir_configuracion_red)

preguntar_ruta_archivo()
leer_webs_archivo(ruta_archivo="web.txt")
leer_ips_webs(ruta_archivo="web.txt")
mostrar_imprimir_configuracion_red()