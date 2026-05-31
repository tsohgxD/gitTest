#!/usr/bin/env python 
import psutil
print("                         Das ist mein PC System info script!!!")
print("                      Hier Sind folgende Infomationen Zum system :")
print("\n\n-Anzahl von CPU cores im system:  ", psutil.cpu_count())


mem = psutil.virtual_memory()
disk = psutil.disk_usage('/')


def bytes_zu_gb(bytes_value):
    return bytes_value / (1024 ** 3)


print("-Total RAM in GB: ",bytes_zu_gb(mem.total))
print("-Wieviel RAM kannst du noch Nutzen: ",bytes_zu_gb(mem.available))
print("-Grösse deiner in GB: ",bytes_zu_gb(disk.total))
print("-Wieviel GB du schon nutzst: ",bytes_zu_gb(disk.used))

