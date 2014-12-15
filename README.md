# RESTful API para la aplicación sun4all version mobil

**Carlos Val Gascón carlos.val@bifi.es**

**System Administrator**


## Introducción
La RESTful API esta localizada en:
```
http://{site-url}/api
``` 
Espera y devolvera siempre un valor de tipo [JSON](http://es.wikipedia.org/wiki/JSON).

## Instalacion

Instalaremos un virtualenv para aislar el sistema. Una vez realizado esta tarea procederemos
a activar el mismo mediante
```
#Creara el entorno virtual
virtualenv flask
#Nos introducimos en el entorno virtual
source/flask/bin/activate
```
### Comprobacion de que el sistema esta levantado
Esta entrada, no esta dentro del RESTful pero sirve para chequear si funciona el sistema, la llamada sera:
```
http://{site-url}
```
El sistema nos tiene que devolver un mensaje de bienvenida.


### Documentacion de las entradas del RESTful
Para la documentacion hemos implementado Swagger en la api que nos permitira tener documentada las 
diferentes entradas de la misma de forma automática.

Para ver la misma simplemente acceda por web a la pagina donde resida la api, en este caso podría ser:
```
http://{site-url}/api
``` 

## Tareas pendientes
- [x] Comprobar Test Units
- [x] Cambiar la llamada de busqueda de imagen por el campo descripcion.
- [x] Grabar datos complementarios del navegador, ip, ...
- [x] Arreglar la grabacion del campo delete a nulo.
- [ ] Nueva entrada de busqueda de imágen por punto.
- [x] Integracion Alembic
- [x] logging and mail alert
