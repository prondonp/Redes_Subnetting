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
        <li></li>
        <li></li>
        <li></li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Richart Smith Escobedo Quispe  - r.escobedo@ulasalle.edu.pe</li>
</ul>
</td>
</<tr>


</td>
</<tr>
<tr><td colspan="6">ALUMNO:
<ul>
<li>Guillermo Jhozua Caceres Rosado  - gcaceresr@ulasalle.edu.pe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

#

## OBJETIVOS Y TEMAS 

### OBJETIVOS

-   Aprender y comprender el patron de diseño designado.
-   Llegar a programar satisfactoriamente el patron en el lenguaje designado.

### TEMAS
-   Reestauracion de estados
-   Comprension del funcionamiento
-   Programación en C++ y Java

## CONTENIDO DE LA GUÍA

### MARCO CONCEPTUAL

-   https://www.w3schools.com/nodejs/nodejs_intro.asp](https://www.w3schools.com/nodejs/nodejs_intro.asp]
-   https://nodejs.org/en/docs/guides/getting-started-guide/](https://refactoring.guru/es/design-patterns/memento/cpp/example)
-   https://nodejs.dev/learn](https://reactiveprogramming.io/blog/es/patrones-de-diseno/memento)
-   https://www.w3schools.com/js/js_api_fetch.asp]
-   http://joaquin.medina.name/web2008/documentos/informatica/documentacion/logica/patrones/patronMemento/2008_08_12_MementoDescripcion.html)
-   https://drive.google.com/file/d/16gzYamgXPApvWk545Az4XlIZfV1W-qP-/view
-   https://reactiveprogramming.io/blog/es/patrones-de-diseno/memento

# INTRODUCCION

El patron de diseño Memento nos permite capturar varios estados con su fecha y hora actuales, para poder volver a ellos mas tarde. Este patrón es utilizado cuando tenemos objetos que cambian en el tiempo y por alguna razón necesitamos restaurar su estado en un momento determinado. 

Un ejemplo claro seria un documento de texto como Word, documentos de google y overleaf. Cada vez que escribimos una letra en el documento de texto se guarda un nuevo estado en el documento, el cual nos permite volver a los estados anteriores guardados o salvados, retrocediendo o adelantando los cambios que hemos hecho.  


![image](https://user-images.githubusercontent.com/74481155/175861611-ea4ae59f-fd34-4ca2-96e6-be57ad5b2e61.png)


Aparte de este ejemplo tambien se utilizan en las actualizaciones de sistema o en un caso mas conocido los video juegos.

Viendolo mas a fondo el patrón Memento se encarga de la creación de capturas instantaneas de estados al propietario de esos estados, el objeto "originador". Por lo tanto, en lugar de que haya otros objetos o usuario intentando copear informacion del originador, la propia clase que edita los datos puede hacerlo, ya que tiene pleno acceso a su propio estado y son los que registra todos los estados ya sea del originador o creador.

El patrón sugiere almacenar la copia del estado del objeto en un objeto especial llamado memento (recuerdo). Los contenidos del memento no son accesibles para ningún otro objeto excepto el que lo produjo o lo creo. Otros objetos deben comunicarse con mementos utilizando una interfaz limitada que pueda permitir extraer los metadatos de la instantánea (tiempo de creación, el nombre de la operación realizada, etc.), pero no el estado del objeto original contenido en la instantánea.


![image](https://user-images.githubusercontent.com/74481155/176829962-fbf3fb9f-714c-460a-b244-03dca761e83f.png)

Los elementos que conforman la grafica son:

 - Memento, almacena/guarda el estado de un objeto del originador/creador, el puede pasarse informacion con la aplicacion para pasarlo a los objetos y al originador/creador para guardar o recordar su estado.
 - Originador, crea al objeot memento para guardar su estado actual o volver al anterior.
 - Aplicacion, mantiene los objetos de memento y originador pero no puede acceder a la informacion para verla o modificarla.

# USOS

- Se usa para salvar el estado en calculos que demoran mucho tiempo en realizar.
- En videojuegos para autoguardarse
- Cuando necesitamos salvar/restaurar el estado de algun objeto o forma.
- Cuando no se desea mostrar el estado directamente.

# PATRONES RELACIONADOS

- Command, este patron utiliza al memento para guardar estados de acciones que no se pueden modificar o hacer
- State, la mayoria de lo estados utilizan el patron memento.

#
#

## EJEMPLO SIMPLE

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
