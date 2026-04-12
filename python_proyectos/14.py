import nmap
scaner=nmap.Portscaner()
ip=input("Ingresa tu direccion ip:")
scaner.scan(ip)
print(scaner.all_hosts())