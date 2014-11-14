# RESTful API para la aplicación sun4all version mobil

**Carlos Val Gascón carlos.val@bifi.es**

**System Administrator**


## Introducción
La RESTful API esta localizada en:
```
http://{site-url}/api
``` 
Espera y devolvera siempre un valor de tipo [JSON](http://es.wikipedia.org/wiki/JSON).


## Servicios
Los estándares de llamadas http que utilizaremos seran los siguiente:
HTTP Metodo Accion Ejemplo

* GET  (Obtiene información de un recurso): http://{site-url}/api/images
* GET  (Obtiene información de un recurso): http://{site-url}/ap/images/2
* POST (Crea un nuevo recurso): http://{site-url}/api/images (con los recursos necesarios)

Vamos a detallar todos los servicios que presta:

### Comprobacion de que el sistema esta levantado
Esta entrada, no esta dentro del RESTful pero sirve para chequear si funciona el sistema, la llamada sera:
```
http://{site-url}
```
El sistema nos tiene que devolver un mensaje de bienvenida.

### Obtencion de todas las imágenes en el sistema.
Corresponde a una llamada de tipo GET que obtiene un listado de todas las imágenes del sistema 

```
http://{site-url}/api/images
```

El sistema te devolvera los datos de esta forma:
```
{
     "images": [
    {
        "browser": null, 
        "created": "Thu, 13 Nov 2014 12:52:23 GMT", 
        "deleted": "", 
        "description": "carlos11", 
        "id": 27, 
        "points": [
            {
                "x": 1.0, 
                "y": 2.0
            }, 
            {
                "x": 1.1, 
                "y": 2.3
            }
           ], 
        "source_ip": null
    },
    {
        "browser": null, 
        "created": "Thu, 13 Nov 2014 12:52:44 GMT", 
        "deleted": "", 
        "description": "carlos11", 
        "id": 28, 
        "points": [
            {
                "x": 1.0, 
                "y": 2.0
            }, 
            {
                "x": 1.1, 
                "y": 2.3
            }
           ], 
        "source_ip": null
    }
}
```
### Obtencion de una imágen por su descripcion
Corresponde a una llamada de tipo GET que obtiene una única imágen 

```
http://{site-url}/api/images/{description}
```

En caso de que encuentre la imágen devolvera la misma en el mismo formato que la entrada anterior 

### Grabación de una imágen
Corresponde a una llamada de tipo POST y se deberán de enviar los parámetros en formato JSON, la llamada tendra que hacerse a la url:

```
http://{site-url}/api/images
```

Y, los parámetros estaran en formato JSON, un ejmplo de envío podría ser:

```
{ 
    "description": 859698212,
    "points": [
        { "x" : 25.36,
          "y" : 36.51
        },

        { "x" : 12.34,
          "y" : 78.22
        },

        { "x" : 67.12,
          "y" : 14.98
        }
    }
}
```

## Tareas pendientes
- [x] Comprobar Test Units
- [x] Cambiar la llamada de busqueda de imagen por el campo descripcion.
- [ ] Grabar datos complementarios del navegador, ip, ...
- [x] Arreglar la grabacion del campo delete a nulo.
- [ ] Nueva entrada de busqueda de imágen por punto.
- [x] Integracion Alembic
- [ ] logging and mail alert
