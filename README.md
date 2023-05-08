# REDES Y COMUNICACION DE DATOS
SUBNETING
<div align="center">
<table>
    <theader>
        <tr>
            <th><img src="https://github.com/rescobedoulasalle/git_github/blob/main/ulasalle.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></th>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD LA SALLE</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍAS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO DE INGENIERÍA Y MATEMÁTICAS</span><br />
                <span style="font-weight:bold;">CARRERA PROFESIONAL DE INGENIERÍA DE SOFTWARE</span>
            </th>            
        </tr>
    </theader>    
</table>
</div>

<div align="center">
<span style="font-weight:bold;">INFORME APLICACION E IMPLEMENTACION SUBNETING</span><br />
  <span style="font-weight:bold;"> </span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>

<tr><td colspan="6">RECURSOS:
    <ul>
        <li>https://drive.google.com/file/d/15MyPhQt9gvHT1a6LxoHExgN79cz7yZ0e/view</li>
        <li>https://www.howtogeek.com/823503/find-subnet-masks-on-linux-ipcalc/</li>
        <li>https://drive.google.com/drive/folders/1YYM8IIoMMiRrhdIaKH90kgFJp3Q-buAr?usp=sharing</li>
        <li>https://keepcoding.io/blog/que-es-subnetting/#:~:text=El%20Subnetting%20o%20subneteo%20es,principal%20y%20a%20un%20mismo%20dominio.</li>
        </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>RICHART SMITH ESCOBEDO QUISPE - r.escobedo@ulasalle.edu.pe</li>
</ul>
</td>
</<tr>


</td>
</<tr>
<tr><td colspan="6">ALUMNO:
<ul>
<li>PEDRO HUMBERTO RONDON PONCE  - prondonp@ulasalle.edu.pe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

#

## OBJETIVOS Y TEMAS 

### OBJETIVOS

-   Aprender la logica y los principales conceptos de Subneting.
-   Comprender la técnica de subdividir una gran red IP física en varias redes lógicas más pequeñas.
-   Implementar adecuadamente Subneting.

### TEMAS
-   Introduccion
-   Conceptos Principales
-   Implementacion en Python

## CONTENIDO DE LA GUÍA


# INTRODUCCION

El Subnetting o subneteo es la técnica de subdividir una gran red IP física en varias redes lógicas más pequeñas, de forma que cada una de estas subnets funcionen como una red individual respecto a envíos y recepción de paquetes, aunque sigan perteneciendo a una misma red principal y a un mismo dominio. Este proceso debe ser realizado cuidadosamente, para así no desaprovechar direcciones IPv4.

Es un procedimiento que permite dividir a una red primaria IPv4 en una serie de subredes, de tal forma que cada una de ellas funcione a nivel de envío y recepción de paquetes, como una red individual, aunque todas pertenezcan a la misma red principal y, por lo tanto, al mismo dominio de difusión original. El proceso de subnetting implica la asignación de bits adicionales a la parte de red de la dirección IP, lo que permite una mayor cantidad de subredes y direcciones IP disponibles. Es importante entender los fundamentos del subnetting para diseñar, configurar y mantener redes informáticas eficientes y seguras.


# Conceptos principales

## Broadcast
También conocido como transmisión o radiodifusión, el broadcast se define como el mensaje transmitido a los integrantes de una red, sin necesidad de retroalimentación. Esta conexión multipunto de una red informática, se encarga de transmitir un paquete de datos a todos los miembros de una red de comunicación, mediante el uso de una dirección de Broadcast.

## Dirección IP
El término dirección IP o dirección de protocolo de internet hace referencia a una representación numérica de la ubicación de un dispositivo en internet o una red local. Funciona como identificador de un dispositivo, y permite el envío de información entre equipos en una red.

## Tipos de IPv4
En la cuarta versión del protocolo de internet, se puede identificar 3 tipos de direcciones IP que se encargan (cada una) del cumplimiento de una tarea específica, siendo estas:

- Direccion Broadcast
Es la última dirección IP dentro de una subred y permite la transmisión de datos a una multitud de nodos receptores que hacen parte de una misma subred.

- Dirección de red
Es la dirección IP a la que se refiere la red o subred. La dirección de red incluye routers en sus tablas de enrutamiento para que puedan llegar a un destino establecido y para poder conocer el origen de un paquete.

- Dirección de Host
Son las direcciones IP (subnetting ip) que se le asignan a los equipos finales de la red y es usada para identificar a un dispositivo particular que esté conectado a la red.

## Subred
Es un rango de direcciones lógica usada para maximizar el espacio de direcciones IPv4. Permiten asignar parte del espacio de la dirección host a las direcciones de red, lo que hace posible que se tengan más redes. A ese espacio de dirección de host asignada a las nuevas direcciones se le denomina número de subred.

## Dirección de subred
Una dirección de subred es utilizada para comparar la dirección del destino de un mensaje con la dirección del sistema principal de origen de este, con el objetivo de establecer si el destino está ubicado en la misma dirección que el origen, o si es posible llegar al destino mediante alguna de las interfaces locales.



# Aplicacion

- Gestión de direcciones IP: El subnetting permite a los administradores de red asignar direcciones IP de manera más eficiente y        controlar el número de dispositivos en una red.

- Segmentación de redes: El subnetting ayuda a dividir grandes redes en segmentos más pequeños, lo que mejora la eficiencia de la red y reduce la congestión.

- Mejora de la seguridad: El subnetting permite a los administradores de red aislar segmentos de la red y aplicar políticas de seguridad específicas a cada subred.

- Optimización del tráfico: El subnetting permite a los administradores de red configurar diferentes políticas de enrutamiento para diferentes subredes, lo que mejora la eficiencia de la red y reduce la congestión.

- Mejora de la gestión de redes: El subnetting facilita la gestión y el monitoreo de redes informáticas, lo que permite a los administradores de red detectar y solucionar problemas de manera más eficiente.


# Implementacion


- Importa las librerías "ipaddress" y "prettytable" que se necesitan para trabajar con direcciones IP y mostrar la información de red en una tabla.
 ```
import ipaddress
from prettytable import PrettyTable
 ```
- Solicita al usuario que ingrese la dirección IP y la cantidad de subredes que desea crear.
 ```
ip = input("Ingrese una dirección IP: ")
num_subnets = int(input("Ingrese la cantidad de subredes: "))
 ```
- Convierte la dirección IP ingresada por el usuario en un objeto de tipo "IPv4Address" para poder trabajar con ella. Crea un objeto de tipo "IPv4Address" a partir de la dirección IP ingresada por el usuario y lo asigna a la variable "ip_addr".
 ```
ip_addr = ipaddress.IPv4Address(ip)
 ```
- La quinta línea obtiene la máscara de red correspondiente a la dirección IP ingresada. Se utiliza la dirección IP ingresada por el usuario (almacenada en la variable "ip_addr") junto con una máscara de red de longitud 24 (que se especifica agregando "/24" al final de la dirección IP) para crear un objeto de tipo "IPv4Network" que representa la red correspondiente. La opción "strict=False" se utiliza para permitir que la dirección IP ingresada no esté en formato de red (por ejemplo, "192.168.0.1" en lugar de "192.168.0.0/24").
El objeto "IPv4Network" creado se almacena en la variable "network", lo que permite utilizarlo para calcular la información de red y las subredes correspondientes.
```
network = ipaddress.IPv4Network(str(ip_addr) + '/24', strict=False)
 ```
- Determinan la clase de la red y calculan la información de red. Wildcard se utiliza para almacenar la máscara inversa (también conocida como wildcard) de la red. La máscara inversa se utiliza en la configuración de redes para indicar qué bits de la dirección IP no están cubiertos por la máscara de red. Se obtiene a través del atributo "hostmask" del objeto "IPv4Network". network_address se utiliza para almacenar la dirección de red de la red. La dirección de red es la dirección IP que se utiliza para identificar la red en la que se encuentra un dispositivo o host. Se obtiene a través del atributo "network_address" del objeto "IPv4Network".
 ```
wildcard = network.hostmask
network_address = network.network_address

if network.is_private:
    network_class = "Privada"
elif network.is_reserved:
    network_class = "Reservada"
elif network.is_global:
    network_class = "Global"
else:
    network_class = "Desconocida"
  ```   
- Calculan la cantidad de bits necesarios para la cantidad de subredes y la cantidad de bits disponibles para los hosts. prefixlen representa la longitud del prefijo de red (en bits) para la dirección IP de la red. El prefijo de red es una parte de la dirección IP que se utiliza para identificar la red y se representa mediante una máscara de subred siendo en este caso /24.
 ```
bits_needed = (num_subnets - 1).bit_length()

bits_available = 32 - network.prefixlen - bits_needed
 ```
- Valida que haya suficientes bits disponibles para los hosts.
 ```
if bits_available < 0:
    print("No hay suficientes bits disponibles para la cantidad de subredes solicitadas.")
 ```
- Obtienen la lista de subredes y hosts por subred y crea una tabla para mostrar los resultados. prefixlen_diff se utiliza para especificar la cantidad de bits adicionales que se necesitan para definir el prefijo de red de cada subred
 ```
else:
    # Obtener la lista de subredes y hosts por subred
    subnets = list(network.subnets(prefixlen_diff=bits_needed))
    hosts_per_subnet = 2**bits_available - 2
 ```
- Agregan filas a la tabla con la información de cada subred, incluyendo la dirección de red, el rango de direcciones IP disponibles para los hosts y la dirección de broadcast.
 ```
 table = PrettyTable()
    table.field_names = ["Subred", "Dirección de red", "Rango de direcciones IP para hosts", "Dirección de broadcast"]
    for i, subnet in enumerate(subnets):
        row = [f"Subred {i+1}", str(subnet.network_address), f"{subnet.network_address+1} - {subnet.broadcast_address-1}", str(subnet.broadcast_address)]
        table.add_row(row)
  ```
- Muestra la información general de la red y la tabla con los detalles de cada subred.
 ```
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
  ```


#



#

##CODIGO 


''''''

    import ipaddress
    from prettytable import PrettyTable
    ip = input("Ingrese una dirección IP: ")
    num_subnets = int(input("Ingrese la cantidad de subredes: "))

    ip_addr = ipaddress.IPv4Address(ip)

    network = ipaddress.IPv4Network(str(ip_addr) + '/24', strict=False)

    wildcard = network.hostmask
    network_address = network.network_address

    if network.is_private:
      network_class = "Privada"
    elif network.is_reserved:
     network_class = "Reservada"
    elif network.is_global:
        network_class = "Global"
    else:
        network_class = "Desconocida"

    bits_needed = (num_subnets - 1).bit_length()

    bits_available = 32 - network.prefixlen - bits_needed

    if bits_available < 0:
        print("No hay suficientes bits disponibles para la cantidad de subredes solicitadas.")
    else:
        subnets = list(network.subnets(prefixlen_diff=bits_needed))
        hosts_per_subnet = 2**bits_available - 2

        table = PrettyTable()
        table.field_names = ["Subred", "Dirección de red", "Rango de direcciones IP para hosts", "Dirección de broadcast"]
    
        # Agregar filas a la tabla
        for i, subnet in enumerate(subnets):
            row = [f"Subred {i+1}", str(subnet.network_address), f"{subnet.network_address+1} - {subnet.broadcast_address-1}",              str(subnet.broadcast_address)]
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
 
''''''


## CONCLUSIONES

El uso de subnetting es esencial en la administración de redes y permite la división de una red grande en varias subredes más pequeñas y manejables. Al dividir una red grande en subredes más pequeñas, se pueden reducir el tráfico de red, mejorar el rendimiento y aumentar la seguridad al limitar el número de hosts en una red. También ayuda a optimizar la asignación de direcciones IP y hace que la administración de direcciones IP sea más eficiente.

La implementación incorrecta del subnetting puede resultar en problemas de red, como la sobrecarga del router o la falta de direcciones IP disponibles. Por lo tanto, es importante entender bien cómo funciona el subnetting y cómo se debe implementar correctamente. En general, el subnetting es una herramienta poderosa para mejorar la gestión de redes, siempre y cuando se implemente adecuadamente y se tenga en cuenta su impacto en el rendimiento y la seguridad de la red.


## REFERENCIAS

-   https://www.ionos.es/digitalguide/servidores/know-how/subnetting-como-funcionan-las-subredes/
-   https://platzi.com/tutoriales/1277-redes-2017/9070-subnetting-que-es-y-como-funciona/
-   https://keepcoding.io/blog/que-es-subnetting/#:~:text=El%20Subnetting%20o%20subneteo%20es,principal%20y%20a%20un%20mismo%20dominio.
-   https://drive.google.com/file/d/15MyPhQt9gvHT1a6LxoHExgN79cz7yZ0e/view
-   https://es.wikipedia.org/wiki/Subred

#

#

# PARTE 3 
## SKILLS FOR ALL CISCO:

![image](https://github.com/prondonp/Redes_Subnetting/blob/9ee68e37f3c0fde594f5a388550c5c169b9793e1/skillsforallcisco.png)

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/
