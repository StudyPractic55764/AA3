import dns.resolver
import time
import statistics
import psutil
import subprocess
import re

def comparacion_dns_archivo(dns_server):

    lista_dns = []
    for linea in dns_server:
        lista_dns.append(linea)

    with open("DNSips.txt", 'r', encoding="utf-8") as archivo:
        for linea_dns in archivo:
            linea_dns = linea_dns.strip()
            lista_dns.append(linea_dns)
    print(lista_dns)

    resultado = []

    for elemento_dns in lista_dns:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = [elemento_dns]
        resolver.timeout = 2
        resolver.lifetime = 2

        tiempo_reaccion = []
        for _ in range(3): 
            try: 
                inicio = time.perf_counter()
                resolver.resolve("google.com", "A")
                fin = time.perf_counter()
                tiempo_reaccion.append((fin - inicio) * 1000)
            except Exception:
                continue
    
        if tiempo_reaccion:
            promedio = sum(tiempo_reaccion) / len(tiempo_reaccion)
            resultado.append({"DNS": elemento_dns, "ms": promedio})
            print(f"DNS {elemento_dns:15} | Latencia media: {promedio:.2f} ms")
        else:
            print(f"DNS {elemento_dns:15} | Error: No hay respuesta")

    resultado.sort(key=lambda x: x["ms"])

    print(f"El DNS más rapida es {resultado[0]['DNS']} con un tiempo de respuesta de {resultado[0]['ms']:.2f} ms")
    return resultado