# Blue-Green deployments 

#### Como construir las imagenes?
Primero necesitamos clonar el repositorio
```sh 
mkdir /docker-files && cd /docker-files
git clone https://github.com/jvimaverick/ML.git
cd ML
```

### Construir la imagen de nginx
```sh
cd /docker-files/ML/nginx
docker build -t juanviola/n1:latest .
```
### Construir la imagen de la app
```sh
cd /docker-files/ML/app
docker build -t juanviola/app:latest .
```

### Pusheamos las imagenes a docker cloud
Como pusheamos las imagenes a docker para que nos queden disponibles en hub.docker.com
```sh
docker login
```
Nos va a pedir un user/pass utilizamos nuestra cuenta de docker hub. Una vez que iniciamos la sesion podemos subir la imagen creada.

```sh
docker push juanviola/n1:latest
docker push juanviola/app:latest
```
#### Como construir el stack en docker cloud?
- Iniciamos la session con nuestra cuenta de docker-cloud en http://cloud.docker.com
- Stack > create > (completamos un nombre) y pegamos el contenido del stack file `docker-cloud-stack.yml`

#### Como ver las estadisticas del haproxy
Ingresando en la url de stats del haproxy, para este ejemplo voy a montarlo en el localhost con ssh. En el docker-host corro 
```sh
docker inspect <haproxy-container-id>
ssh -L 1936:<ip-container>:9000 <ssh-ip-of-docker-host>
ssh -L 1936:172.17.0.10:9000 nginx
````
En un browser ahora accedo a http://localhost:9000/stats (user/pass: stats/stats)

#### Como ver mas informacion de los logs
Instalo goaccess y corro contra los logs que tengo exportados.
```sh
goaccess -a -f /docker-files/ML/nginx/logs/nginx-access-n1.log
```
#### Como testeo si los cambios de configuracion estan ok?
Una opcion seria levantando el contenedor y corro los test contra la url publica, si funciona lo coloco dentro del balancer de nuevo.

Hice un simple script en python para verificar que los endpoints esten respondiendo de manera correcta
```sh
nginx-test.py http://example.com; echo $?
```

#### Routing
![Routing Example](https://github.com/jvimaverick/ML/blob/master/routing.png)

Autor
----
Juan M V.

