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


![image](https://user-images.githubusercontent.com/74481155/175861611-ea4ae59f-fd34-4ca2-96e6-be57ad5b2e61.png)

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


![image](https://user-images.githubusercontent.com/74481155/176829962-fbf3fb9f-714c-460a-b244-03dca761e83f.png)



# Aplicacion

- Gestión de direcciones IP: El subnetting permite a los administradores de red asignar direcciones IP de manera más eficiente y        controlar el número de dispositivos en una red.

- Segmentación de redes: El subnetting ayuda a dividir grandes redes en segmentos más pequeños, lo que mejora la eficiencia de la red y reduce la congestión.

- Mejora de la seguridad: El subnetting permite a los administradores de red aislar segmentos de la red y aplicar políticas de seguridad específicas a cada subred.

- Optimización del tráfico: El subnetting permite a los administradores de red configurar diferentes políticas de enrutamiento para diferentes subredes, lo que mejora la eficiencia de la red y reduce la congestión.

- Mejora de la gestión de redes: El subnetting facilita la gestión y el monitoreo de redes informáticas, lo que permite a los administradores de red detectar y solucionar problemas de manera más eficiente.


# Implementacion

- Se agrega la clase Originator/Creador llamado "EmpleadosDatos", donde se encuentran propiedades del estado con metodos set y get. Aparte se agrera el "import java.io*" para poder imprimir un argumento que va pasando.

    ```sh
    import java.io.*;

    public class EmpleadosDatos {
    
    private String nombre, apellido, numero_de_empleado;
    
    public void setNombre(String nombre) {
        Sytem.out.println("Nombre "+ nombre);
        this.nombre = nombre;
    }
    
    public void setApellido(String apellido) {
        Sytem.out.println("Apellido "+ apellido);
        this.apellido = apellido;
    }
    
    public void setNumeroDeEmpleado(String numero_de_empleado) {
        Sytem.out.println("Numero de empleado "+ numero_de_empleado);
        this.numero_de_empleado = numero_de_empleado;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public String getApellido() {
        return apellido;
    }
    
    public String getNumeroDeEmpleado() {
        return numero_de_empleado;
    }
    
    ```
    
- Se crea el Memento para guardar los datos nombre, apellido y numero de empleado.
    
    ```sh
    public Memento GuardaMemetno() {
        System.out.println("\nGuardando estado --\n");
        return new Memento(nombre, apellido, numero_de_empleado);
    }
     ```
     
- Se crea el void para restaurar los datos del Memento.     
     
    ```sh
    public void RestaurarMemento(Memento memento) {
        System.out.println("\nRestaurar estado --\n");
        this.setNombre(memento.getNombre());
        this.setApellido(memento.getApellido());
        this.setNumeroDeEmpleado(memento.getNumeroDeEmpleado());
     }
    }
    ```
    
- Se crea la clase Memento que guardara los estados de los objeto, se crea el constructor de la clase de datos de los empleados.

    ```sh
    import java.io.*;


    public class Memento {
    
    private String nombre;
    private String apellido;
    private String numero_de_empleado;
    
    public Memento(String nombre, String apellido, String numero_de_empleado) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numero_de_empleado = numero_de_empleado;
    }
    ```
    
- Se crea los metodos get() y set() dentro de la clase Memento.

    ```sh 
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public void setApellido(String apellido) {
        this.apellido = apellido;
    }
    
    public void setNumeroDeEmpleado(String numero_de_empleado) {
        this.numero_de_empleado = numero_de_empleado;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public String getApellido() {
        return apellido;
    }
    
    public String getNumeroDeEmpleado() {
        return numero_de_empleado;
    }
    }
    }
    ```

- Se crea la clase Almacen/Caretaker para que cuide de los datos almacenados en Memento y asi no se pueda extraer la informacion por terceros.

    ```sh
    import java.io.*;

    public class Almacen {
    
    private Memento memento;
    
    public void setMemento (Memento memento) {
        this.memento = memento;
    }
    
    public Memento getMemento() {
        return memento;
    }
    }
    ```
    
- Por ultimo se crea la clase Main para que llame a las demas clases creadas (EmpleadosData, Memento, Almacen) para poder ejecutar el programa.

   ```sh
   public class Main {
    public static void main(String[] args) {
   ```


- En este mismo se crea el objeto de datos de empleados y se le introduce las propiedades/Datos

   ```sh
   EmpleadosDatos ed = new EmpleadosDatos();
        ed.setNombre("Guillermo");
        ed.setApellido("Caceres");
        ed.setNumeroDeEmpleado("555");
   ```

- Se llama a la clase almacen para guardar el estado.

   ```sh
   Almacen m = new Almacen();
        m.setMemento(ed.GuardaMemento());
   ```

- El estado vuelve al actual y cambio el Originador/Creador cuando se añaden mas datos.

   ```sh
   ed.setNombre("Juan");
        ed.setApellido("Torres");
        ed.setNumeroDeEmpleado("1054");
        
        ed.setNombre("Maryori");
        ed.setApellido("Calcin");
        ed.setNumeroDeEmpleado("145");
        
        ed.setNombre("Jose");
        ed.setApellido("Barrios");
        ed.setNumeroDeEmpleado("7894");
   ```

- Se restaura el estado guardado antes de introducir los demas

   ```sh
   ed.RestaurarMemento(m.getMemento());
        
    }
   }
   ```

## EJEMPLO COMPLEJO

- Se agrega las librerias correspondientes para el funcionamiento del codigo, como chrono para implementar el tiempo y fecha del guardado entre otros mas.

    ```sh
    #include<iostream>
    #include<fstream>
    #include<stdio.h>
    #include <chrono>
    #include <ctime> 
    #include <vector>
    ```
- Creamos la clase Memento el cual nos proporciona un interfaz para poder recuperar datos o estados anteriores. La fecha de creacion o el nombre de quien lo guarde o pertenezca los datos

    ```sh
    using namespace std;
 
    class Memento{
    public:
    virtual std::string GetName() const = 0;
    virtual std::string dato() const = 0;
    virtual std::string estado() const = 0;
    };
    ```
- Creamos la clase MementoConcreto donde se encuentra la estructura para almacenar los estados del creador, donde escribimos los estados y datos.
Llamamos a la clase para escribir el estado actual del creador y el tiempo actual en publico.
    
    ```sh
    class MementoConcreto : public Memento{
    private:
    std::string estado_;
    std::string dato_;

    public:
    MementoConcreto(std::string estado) : estado_(estado) {
    this->estado_ = estado;
    std::time_t now = std::time(0);
    this->dato_ = std::ctime(&now);
    }
    ```
- Se usa el metodo override para restaurar una version anterior al actual. 
    
    ```sh
    std::string estado() const override {
    return this->estado_;
    }
    ```
- Estos metodos se utilizan para pasar la informacion a Almacen para que pueda utilizarlos y guardarlos. 
    
    ```sh
    std::string GetName() const override {
    return this->dato_ + " / (" + this->estado_.substr(0, 9) + "...)";
    }
    std::string dato() const override {
    return this->dato_;
    }
    };
    ```
    
- Se crea la clase Creador en el cual se definen las funciones memento y otro para volver al estado anterior, el estado inicial se almacena dentro de una sola variable en la funcion.

- Se utiliza el GeneradorRandomString para que en cada compilacion nos escriba un estado distinto al anterior y tambien medir la cantidad de estos
    
    ```sh
    class Creador {
    private:
    std::string estado_;

    std::string GeneradorRandomString(int length = 10) {
    const char alphanum[] =
        "REUNION CON PROGRAMADORES"
        "CORRIGIENDO EL SERVIDOR"
        "VERIFICANDO LAS ACTUALIZACIONES";
    int stringLength = sizeof(alphanum) - 1;

    std::string random_string;
    for (int i = 0; i < length; i++) {
      random_string += alphanum[std::rand() % stringLength];
    }
    return random_string;
    }

    public:
    Creador(std::string estado) : estado_(estado) {
    std::cout << "Creador: Mi estado inicial es: " << this->estado_ << "\n";
    }
    ```
    
- Se crea la funcion Hacer_algo cuando se mostrar el cambio de las actividades o estados del creador.

- Aparte se crea el puntero Guardar en Memento con la cual se guarda una copia de seguridad en el mismo. Tambien se guarda los datos del puntero en un memento indicando que es el estado actual del creador.
    
    ```sh
    void Hacer_algo() {
    std::cout << "Creador: estoy haciendo algo importante.\n";
    this->estado_ = this->GeneradorRandomString(30);
    std::cout << "Creador: y mi estado ha cambiado a: " << this->estado_ << "\n";
    }
    
    Memento *Guardar() {
    return new MementoConcreto(this->estado_);
    }
    
    void Restaurar(Memento *memento) {
    this->estado_ = memento->estado();
    std::cout << "Creador: Mi estado ha cambiado a: " << this->estado_ << "\n";
    }
    };
    ```
    
- Se crea la clase almacen la cual la volvemos independiente de la clase MementoConcreto, por lo que no tiene acceso al estado original del Creador. Pero si los siguientes estados a los que va cammbiando.

- Aqui mismo se incluye la funcion de deshacer un estado y volver al anterior que esta ligada a la funcion de Restaurar.
    
    ```sh
    class Almacen {
    
    private:
    std::vector<Memento *> mementos_;
    
    Creador *creador_;

    public:
    Almacen(Creador *creador) : creador_(creador) {
    this->creador_ = creador;
    }

    void Respaldo() {
    std::cout << "\nAlmacen: Salvando el estado del creador...\n";
    this->mementos_.push_back(this->creador_->Guardar());
    }
    
    void Deshacer() {
    if (!this->mementos_.size()) {
      return;
    }
    
    Memento *memento = this->mementos_.back();
    this->mementos_.pop_back();
    std::cout << "Almacen: Restaurando el estado a: " << memento->GetName() << "\n";
    try {
      this->creador_->Restaurar(memento);
    } catch (...) {
      this->Deshacer();
    }
    }
    
    void Historial() const {
    std::cout << "Almacen: Aqui esta la lista de recuerdos.:\n";
    for (Memento *memento : this->mementos_) {
      std::cout << memento->GetName() << "\n";
    }
    }
    };
    ```
- Se crea la funcion para la interfaz del usuario donde indicamos el estado actual de creador en el memento y para que el almacen guarde sus estados que va ingresando.

- El usuario pedira los estados anteriores del creador para lo cual se llama la funcion de Deshacer.
    
    ```sh
    void CodigoUsuario() {
    Creador *creador = new Creador("Inicio-incial-del-dia");
    Almacen *almacen = new Almacen(creador);
    almacen->Respaldo();
    creador->Hacer_algo();
    almacen->Respaldo();
    creador->Hacer_algo();
    almacen->Respaldo();
    creador->Hacer_algo();
    std::cout << "\n";
    almacen->Historial();
    std::cout << "\nUsuario: Volvamos un estado antes\n\n";
    almacen->Deshacer();
    std::cout << "\nUsuario: Volvamos dos estados antes\n\n";
    almacen->Deshacer();

    delete creador;
    delete almacen;
    }
    ```
- En el int main llamamos a todo la funcion del CodigoUsuario para poder ejecutarlo
    
    ```sh
    int main() {
    std::srand(static_cast<unsigned int>(std::time(NULL)));
    CodigoUsuario();
    return 0;
    }
    ```

#



#

## CONCLUSIONES

### FAVORABLE

-  Puedes producir capturas de los estados del objeto sin atravesar su encapsulación.
-  Puedes simplificar el código del originador/creador permitiendo que la cuidadora/alamacen mantenga el historial del estado del originador/creador.

### DESFAVORABLE

-  La aplicación puede consumir mucha memoria RAM si los clientes crean mementos muy a menudo y no tienen en cuenta su consumo excesivo.
-  El cuidador/alamacen deben seguir el ciclo de vida del originador/creador para poder destruir mementos obsoletos.
-  La mayoría de los lenguajes de programación dinámicos, como PHP, Python y JavaScript, no pueden garantizar que el estado dentro del memento se mantenga intacto ya que aveces puede resultar modificaciones.

## CONSECUENCIAS

El patrón Memento tiene varias consecuencias:

-  Preservación de los límites de la encapsulación. El elemento se mantiene guardado asi evitando que todos los objetos o participantes del programa puedan ver o modificar la informacion guardad en el memento.
-  Simplifica al Creador. Se conserva la encapsulacion y el creador/originador mantiene sus estados solicitados por el usuario. 
-  El uso de mementos puede ser costoso. Los mementos producen un costo considerable cuando el creador/originador recibe mucha informacion por para recordar de los usuarios.
-  Definición de interfaces reducidas y amplias. En algunos lenguajes puede ser difícil garantizar que sólo el creador acceda al estado del memento.
-  Costes ocultos en el cuidado de los mementos. 

#

## REFERENCIAS

-   https://www.w3schools.com/nodejs/nodejs_intro.asp](https://www.w3schools.com/nodejs/nodejs_intro.asp]
-   https://nodejs.org/en/docs/guides/getting-started-guide/](https://refactoring.guru/es/design-patterns/memento/cpp/example)
-   https://nodejs.dev/learn](https://reactiveprogramming.io/blog/es/patrones-de-diseno/memento)
-   https://www.w3schools.com/js/js_api_fetch.asp]
-   http://joaquin.medina.name/web2008/documentos/informatica/documentacion/logica/patrones/patronMemento/2008_08_12_MementoDescripcion.html)
-   https://drive.google.com/file/d/16gzYamgXPApvWk545Az4XlIZfV1W-qP-/view
-   https://reactiveprogramming.io/blog/es/patrones-de-diseno/memento
-   https://www.youtube.com/watch?v=VCZK62hXz3E
-   https://github.com/mitocode21/patrones-diseno/tree/master/Memento

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
