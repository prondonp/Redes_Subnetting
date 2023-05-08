import ipaddress
from prettytable import PrettyTable

# Solicitar al usuario que ingrese la dirección IP y la cantidad de subredes
ip = input("Ingrese una dirección IP: ")
num_subnets = int(input("Ingrese la cantidad de subredes: "))

# Convertir la dirección IP en un objeto IPv4Address
ip_addr = ipaddress.IPv4Address(ip)

# Obtener la máscara de red correspondiente a la dirección IP
network = ipaddress.IPv4Network(str(ip_addr) + '/24', strict=False)

# Calcular la información de red
wildcard = network.hostmask
network_address = network.network_address

# Determinar la clase de la red
if network.is_private:
    network_class = "Privada"
elif network.is_reserved:
    network_class = "Reservada"
elif network.is_global:
    network_class = "Global"
else:
    network_class = "Desconocida"

# Calcular la cantidad de bits necesarios para la cantidad de subredes
bits_needed = (num_subnets - 1).bit_length()

# Calcular la cantidad de bits disponibles para los hosts
bits_available = 32 - network.prefixlen - bits_needed

# Validar que haya suficientes bits disponibles para los hosts
if bits_available < 0:
    print("No hay suficientes bits disponibles para la cantidad de subredes solicitadas.")
else:
    # Obtener la lista de subredes y hosts por subred
    subnets = list(network.subnets(prefixlen_diff=bits_needed))
    hosts_per_subnet = 2**bits_available - 2

    # Crear tabla para mostrar los resultados
    table = PrettyTable()
    table.field_names = ["Subred", "Dirección de red", "Rango de direcciones IP para hosts", "Dirección de broadcast"]
    
    # Agregar filas a la tabla
    for i, subnet in enumerate(subnets):
        row = [f"Subred {i+1}", str(subnet.network_address), f"{subnet.network_address+1} - {subnet.broadcast_address-1}", str(subnet.broadcast_address)]
        table.add_row(row)

    # Mostrar la tabla
    print("Dirección IP: ", ip)
    print("Máscara de red: ", network.netmask)
    print("Wildcard: ", wildcard)
    print("Dirección de red: ", network_address)
    print("Clase de la red: ", network_class)
    print("Cantidad de subredes solicitadas: ", num_subnets)
    print("Bits necesarios para las subredes: ", bits_needed)
    print("Bits disponibles para los hosts: ", bits_available)
    print("Cantidad de hosts por subred: ", hosts_per_subnet)
    print(table)
 