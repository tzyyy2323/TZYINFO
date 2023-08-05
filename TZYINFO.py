import platform
import psutil
import random
import time
import GPUtil
import tabulate 
import subprocess
import distutils
import math
import os
from datetime import datetime
import sys

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# INTRODUCCIÓN DE MI TRABAJO

print("""
    
      
      
      TZYINFO... BIENVENIDO /// WELCOME
      
      
      
▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
      
      
      
      
      """) 

# AQUÍ SE ELIGE LA INFORMACIÓN QUE QUIERE VER 

print("="*40, "Indique la información que desea ver", "="*44)

eleccion = 0
while eleccion !=10:
    print("""
          1- INFORMACIÓN DEL SISTEMA
          
          2- INFORMACIÓN DEL CPU

          3- TEMPERATURA DEL CPU [SOLO LINUX]
          
          4- INFORMACIÓN DE LA TARJETA GRÁFICA [SOLO NVIDIA]
          
          5- INFORMACIÓN DE LA MEMORIA
          
          6- INFORMACIÓN DEL DISCO DURO
          
          7- INFORMACIÓN DE LAS REDES
          
          8- CRÉDITOS
          
          9- SALIR

          10- CHANGE LANGUAGE /// CAMBIAR IDIOMA
          """)

    # INFORMACIÓN DEL SISTEMA
    
    eleccion = float(input())
    if eleccion == 1:
        print("")
        print("="*40, "Información del Sistema", "="*40)
        uname = platform.uname()
        print(f"Sistema ===> {uname.system}") 
        print("="*40)   
        print(f"Nombre del Nodo ===> {uname.node}")
        print("="*40)
        print(f"Versión de lanzamiento ===> {uname.release}")
        print("="*40)
        print(f"Versión ===> {uname.version}")
        print("="*40)
        print(f"Arquitectura ===> {uname.machine}")
        print("="*40)
        print(f"Procesador ===> {uname.processor}") 
        print("="*100)

    # INFORMACIÓN DEL CPU

    if eleccion == 2:
        print("")
        print("="*40, "Información de la CPU", "="*40)
        print("Núcleos físicos ===>", psutil.cpu_count(logical=True))
        print("="*40)
        cpufreq = psutil.cpu_freq()
        print(f"Frecuencia máxima ===> {cpufreq.max:.2f}Mhz")
        print("="*40)
        print(f"Frecuencia mínima ===> {cpufreq.min:.2f}Mhz")
        print("="*40)
        print(f"Frecuencia actual ===> {cpufreq.current:2f}Mhz")
        print("="*40)
        print("Uso del CPU por núcleo")
        print("="*40)
        for i, percentage in enumerate (psutil.cpu_percent(percpu=True)):
            print(f"Núcleo /// Core {i} ==> {percentage}%")
            print("="*40)                
            print(f"Uso total del CPU ===> {psutil.cpu_percent()}%")
            print("="*100)
            
    # TEMPERATURA DE LA CPU (LINUX)
    
    if eleccion == 3:
        print("="*40, "Temperatura del CPU", "="*40)
        def get_cpu_temperature():
                cpu_temperature = psutil.sensors_temperatures()['coretemp'][0].current
                return cpu_temperature
        print("Temperatura de CPU ===>", get_cpu_temperature(), "°C")


    # INFORMACIÓN DE LA TARJETA GRÁFICA

    if eleccion == 4:
        print("="*40, "Información de la Tarjeta Gráfica", "="*40)
        gpus = GPUtil.getGPUs()
        list_gpus = []
        for gpu in gpus:
                gpu_id = gpu.id
                gpu_name = gpu.name
                gpu_load = f"{gpu.load*100}%"
                gpu_free_memory = f"{gpu.memoryFree}MB"
                gpu_used_memory = f"{gpu.memoryUsed}MB"
                gpu_total_memory = f"{gpu.memoryTotal}MB"
                gpu_temperature = f"{gpu.temperature} °C"
                gpu_uuid = gpu.uuid
        
        print(f"ID de la Tarjeta Gráfica ===> {gpu.id}")
        print("="*40)
        print(f"Nombre de la Tarjeta Gráfica ===>  {gpu.name}")
        print("="*40)
        print(f"GPU UUID ===> {gpu.uuid}")
        print("="*40)
        print(f"Uso actual ===>  {gpu.load*100}%")
        print("="*40)
        print(f"Memoria VRAM total ===>  {gpu.memoryTotal}MB")
        print("="*40)
        print(f"Memoria VRAM usada ===> {gpu.memoryUsed}MB")
        print("="*40)
        print(f"Memoria VRAM libre ===>  {gpu.memoryFree}MB")
        print("="*40)
        print(f"Temperatura actual ===>  {gpu.temperature}°C")
        print("="*100)
        
    # INFORMACIÓN DE LA MEMORIA RAM

    if eleccion == 5:
        print("")
        print("="*40 ,"Información de la Memoria", "="*40)
        svmem = psutil.virtual_memory()
        print(f"Memoria Total ===> {get_size(svmem.total)}")
        print("="*40)
        print(f"Disponible ===> {get_size(svmem.available)}")
        print("="*40)
        print(f"Usado ===> {get_size(svmem.used)}")
        print("="*40)
        print(f"Porcentaje ===> {get_size(svmem.percent)}%")
        print("="*100)

    # INFORMACIÓN DE LOS DISCOS DUROS

    if eleccion == 6:
        print("")
        print("="*40 ,"Información del Disco Duro", "="*40)
        print("PARTICIONES Y USO:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f" === Dispositivo ===> {partition.device}")
            print(f" Punto de montaje ===> {partition.mountpoint}")
            print(f" Tipo de sistema de archivo ===> {partition.fstype}")
            print("="*40)
       
    #  INFORMACIÓN DE LAS REDES

    if eleccion == 7:
        print("")
        print("="*40, "Información de Red", "="*40)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interfaz ===> {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  Dirección IP ===> {address.address}")
                    print(f"  Máscara de Red ===> {address.netmask}")
                    print(f"  Transmisión de IP ===> {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  Dirección MAC ===> {address.address}")
                    print(f"  Máscara de Red ===> {address.netmask}")
                    print(f"  Transmisión de MAC ===> {address.broadcast}")

   # CRÉDITOS

    if eleccion == 8:
        print("""
        CREADO POR LUIS DIEGO
        TZYYY
    
    …………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                  
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄                               
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀

        
              """)
        
# EXIT

if eleccion == 9:
    sys.exit(1)
    
# CAMBIO DE IDIOMA

if eleccion == 10:
    print("="*30, "PARA VOLVER AL IDIOMA ESPAÑOL DEBE CERRAR EL PROGRAMA", "="*30)
    print("="*30, "TO GO BACK TO THE SPANISH LANGUAGE YOU MUST CLOSE THE PROGRAM", "="*22)

# =======================================================================================================

# SE REESCRIBE TODO EL CÓDIGO EN INGLÉS

    print("""
    
      
      
      TZYINFO... WELCOME
      
      
      
▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒
▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒
▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒
▒▒▒▒▒███░░▐█░█▌░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌
▒▒▒▒████░▐█▌░▐█▌██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▐████░▐░░░░░▌██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░▄█░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████░░░██░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒████▌░▐█░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▐████░░▌░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
█████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
      
      
      
      
      """) 

print("="*40, "Indicate the information you want to see", "="*40)

eleccioning = 0
while eleccioning !=9:
    print("""
          1- SYSTEM INFORMATION
          
          2- CPU INFORMATION
          
          3- CPU TEMPERATURE [ONLY LINUX]
          
          4- GPU INFORMATION [ONLY NVIDIA]
          
          5- MEMORY INFORMATION
          
          6- DISK DRIVE INFORMATION
          
          7- NETWORK INFORMATION
          
          8- CREDITS
          
          9- EXIT
          """)
    eleccioning = float(input())

    if eleccioning == 1:
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print("")
        print(f"System ===> {uname.system}")
        print("="*40)
        print(f"Node Name ===> {uname.node}")
        print("="*40)
        print(f"Release ===> {uname.release}")
        print("="*40)
        print(f"Version ===> {uname.version}")
        print("="*40)
        print(f"Machine ===> {uname.machine}")
        print("="*40)
        print(f"Processor ===> {uname.processor}")
        print("="*100)

    if eleccioning == 2:
        print("="*40, "CPU Information", "="*40)
        print("")
        print("Physical cores ===>", psutil.cpu_count(logical=False))
        print("Total cores ===>", psutil.cpu_count(logical=True))
        print(f"Max Frequency ===> {cpufreq.max:.2f}Mhz")
        print(f"Min Frequency ===> {cpufreq.min:.2f}Mhz")
        print(f"Current Frequency ===> {cpufreq.current:.2f}Mhz")
        print("CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i} ===> {percentage}%")
            print(f"Total CPU Usage ===> {psutil.cpu_percent()}%")
    

    if eleccioning == 3:
        print("="*40, "CPU Temperature", "="*40)
        print("")
        def get_cpu_temperature():
                cpu_temperature = psutil.sensors_temperatures()['coretemp'][0].current
                return cpu_temperature
        print("CPU Temperature ===>", get_cpu_temperature(), "°C")
        

    if eleccioning == 4:
        print("="*40, "GPU Information [ONLY NVIDIA]", "="*40)
        print("")
        
        print(f"GPU ID ===> {gpu.id}")
        print("="*40)
        print(f"GPU name ===>  {gpu.name}")
        print("="*40)
        print(f"GPU UUID ===> {gpu.uuid}")
        print("="*40)
        print(f"Current usage ===>  {gpu.load*100}%")
        print("="*40)
        print(f"Total VRAM ===>  {gpu.memoryTotal}MB")
        print("="*40)
        print(f"Used VRAM ===> {gpu.memoryUsed}MB")
        print("="*40)
        print(f"Free VRAM ===>  {gpu.memoryFree}MB")
        print("="*40)
        print(f"Current temperature ===>  {gpu.temperature}°C")
        print("="*100)


    if eleccioning == 5:
        print("="*40, "Memory Information", "="*40)
        print("")
        print(f"Total memory ===> {get_size(svmem.total)}")
        print("="*40)
        print(f"Available ===> {get_size(svmem.available)}")
        print("="*40)
        print(f"Used ===> {get_size(svmem.used)}")
        print("="*40)
        print(f"Percentage ===> {get_size(svmem.percent)}%")
        print("="*100)

    if eleccioning == 6:
        print("="*40, "Disk Dive Information", "="*40)
        print("")
        print("="*40 ,"Información del Disco Duro /// Disk Drive Information", "="*40)
        print("PARTICIONES Y USO /// PARTITIONS AND USAGE:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f" === Dispositivo /// Device ===> {partition.device}")
            print(f" Punto de montaje /// Mountpoint ===> {partition.mountpoint}")
            print(f" Tipo de sistema de archivo /// File system type ===> {partition.fstype}")
            print("="*40)
    
    if eleccioning == 7:
        print("="*40, "Network Information", "="*40)
        print("")
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface ===> {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address ===> {address.address}")
                    print(f"  Netmask ===> {address.netmask}")
                    print(f"  Broadcast IP ===> {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address ===> {address.address}")
                    print(f"  Netmask ===> {address.netmask}")
                    print(f"  Broadcast MAC ===> {address.broadcast}")

    if eleccioning == 8:
        print("""
        MADE BY LUIS DIEGO
        TZYYY
    
    …………………▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                  
……………▄▄█▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓█▄▄                               
…………▄▀▀▓▒░░░░░░░░░░░░░░░░▒▓▓▀▄
………▄▀▓▒▒░░░░░░░░░░░░░░░░░░░▒▒▓▀▄
……..█▓█▒░░░░░░░░░░░░░░░░░░░░░▒▓▒▓█
…..▌▓▀▒░░░░░░░░░░░░░░░░░░░░░░░░▒▀▓█
…..█▌▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
…▐█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█▌
…█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█
..█▐▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█▓█
…█▓█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▌▓█
..█▓▓█▒░░░░▒█▄▒▒░░░░░░░░░▒▒▄█▒░░░░▒█▓▓█
..█▓█▒░▒▒▒▒░░▀▀█▄▄░░░░░▄▄█▀▀░░▒▒▒▒░▒█▓█
.█▓▌▒▒▓▓▓▓▄▄▄▒▒▒▀█░░░░█▀▒▒▒▄▄▄▓▓▓▓▒▒▐▓█
.██▌▒▓███▓█████▓▒▐▌░░▐▌▒▓████▓████▓▒▐██
..██▒▒▓███▓▓▓████▓▄░░░▄▓████▓▓▓███▓▒▒██
..█▓▒▒▓██████████▓▒░░░▒▓██████████▓▒▒▓█
..█▓▒░▒▓███████▓▓▄▀░░▀▄▓▓███████▓▒░▒▓█
….█▓▒░▒▒▓▓▓▓▄▄▄▀▒░░░░░▒▀▄▄▄▓▓▓▓▒▒░▓█
……█▓▒░▒▒▒▒░░░░░░▒▒▒▒░░░░░░▒▒▒▒░▒▓█
………█▓▓▒▒▒░░██░░▒▓██▓▒░░██░░▒▒▒▓▓█
………▀██▓▓▓▒░░▀░▒▓████▓▒░▀░░▒▓▓▓██▀
………….░▀█▓▒▒░░░▓█▓▒▒▓█▓▒░░▒▒▓█▀░
…………█░░██▓▓▒░░▒▒▒░▒▒▒░░▒▓▓██░░█
………….█▄░░▀█▓▒░░░░░░░░░░▒▓█▀░░▄█
…………..█▓█░░█▓▒▒▒░░░░░▒▒▒▓█░░█▓█
…………….█▓█░░█▀█▓▓▓▓▓▓█▀░░█░█▓█▌
……………..█▓▓█░█░█░█▀▀▀█░█░▄▀░█▓█
……………..█▓▓█░░▀█▀█░█░█▄█▀░░█▓▓█
………………█▓▒▓█░░░░▀▀▀▀░░░░░█▓▓█
………………█▓▒▒▓█░░░░ ░░░░░░░█▓▓█
………………..█▓▒▓██▄█░░░▄░░▄██▓▒▓█
………………..█▓▒▒▓█▒█▀█▄█▀█▒█▓▒▓█
………………..█▓▓▒▒▓██▒▒██▒██▓▒▒▓█
………………….█▓▓▒▒▓▀▀███▀▀▒▒▓▓█
……………………▀█▓▓▓▓▒▒▒▒▓▓▓▓█▀
………………………..▀▀██▓▓▓▓██▀

        
              """)
        
    if eleccioning == 9:
        print("""
        THANKS FOR USE MY APP
        MADE BY TZYYY
        """)
        sys.exit(1)

        





