# RESTful API para la aplicación sun4all version mobil

**Carlos Val Gascón carlos.val@bifi.es**

**System Administrator**


## Introducción
La RESTful API esta localizada en:
```
http://{site-url}/api
``` 
Espera y devolvera siempre un valor de tipo[JSON](http://es.wikipedia.org/wiki/JSON).


## Servicios
Los estándares de llamadas http que utilizaremos seran los siguiente:
HTTP Metodo Accion Ejemplo

* GET  (Obtiene información de un recurso): http://{site-url}/api/images
* GET  (Obtiene información de un recurso): http://{site-url}/ap/images/2
* POST (Crea un nuevo recurso): http://{site-url}/api/images (con los recursos necesarios)

Vamos a detallar todos los servicios que presta:

1. Comprobacion de que el sistema esta levantado
   Esta entrada, no esta dentro del RESTful pero sirve para chequear si funciona el sistema, la llamada sera:

   ```
   http://{site-url}
   ```

   El sistema nos tiene que devolver un mensaje de bienvenida.




## Tareas Pendientes
- [X] ...

