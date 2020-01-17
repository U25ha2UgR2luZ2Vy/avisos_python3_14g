# Proyecto #01 `HTTP Bruteforcer`
Unicamente debe realizar el escaneo a partir de la url que se le indica a directorios mas profundos, es decir, si se envia como parámetro la url http://algo.com/archivos/ no debe buscar en directorios mas externos o del mismo nivel por ejemplo: 
http://algo.com/ o http://algo.com/imagenes/

Debe entrar a los directorios mas profundos, es decir, si se envía la siguiente url como parámetro http://algo.com/archivos/ y se encuentra el recurso http://algo.com/archivos/_vti_bin/_vti_adm/admin.dll deberá buscar en http://algo.com/archivos/_vti_bin/
y en http://algo.com/archivos/_vti_bin/_vti_adm/

*Nota: Recordar que el index of es un directorio, se debe indicar en el reporte que el recurso en cuestion tiene un listado de directorios y ya no debe buscar mas recursos sobre el ejemplo de un index of https://impacto.mx/tag/ entonces en el reporte en la parte de hallazgos deberian poner algo como directorio,indexof,https://impacto.mx/tag/.
# Proyecto #02 `Web Crawler`
Se deberá generar un archivo HTML en donde se imprima el arbol de las urls recuperadas como lo hace el comando tree de linux sin hacer uso de modulos y ademas las urls deben ser colocadas de manera tal que al dar clic en ellas se pueda acceder al recurso.
NOTA: El crawleo solo debe considerar urls del dominio que se esta crawleando por ejemplo si se esta crawleando unam.mx y se encuentran urls de youtube.com o de cualquier otro lado ignorenlas, al igual que los subdominios como ingenieria.unam.mx.
# Proyecto #03 `Apache2 Logs`
El programa debera ser capaz de recibir la/las bitacoras con las que va a trabajar con la misma bandera considerando 3 casos:
- Caso 1 Único Archivo: --file apache.log
- Caso 2 Múltiples Archivos: --file apache1.log,apache2.log,apache3.gz
- Caso 3 Directorio: --file /var/log/apache2/logs/
# Proyecto #04 `Port Scanner`
Determinar los servicios y/o version de los mismos a partir del banner en las respuestas.
# Proyecto #05 `Twitter Analyzer`
El archivo HTML debera contener toda la informacion obtenida incluyendo las imagenes y graficas generadas.