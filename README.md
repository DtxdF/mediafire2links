# mediafire2links
Obtén los enlaces de descarga, ya sea de un único archivo o una carpeta entera que estén alojados en mediafire.

# Dependencias

* lxml
* bs4
* requests

# Pasos para la obtención

El script ejecutará una serie de pasos dependiendo del tipo de archivo. En el caso de una carpeta, se debe colocar explícitamente, ya sea en minúscula o en mayúscula, una letra; 'D' para las carpetas y 'F' para los archivos individuales. Pero que mejor manera de demostrar que una situación práctica:

**Obtener enlace de un archivo:**

```bash
python3 mediafire2links.py f https://www.mediafire.com/file/[Irrelevante]/[Nombre del archivo]/file
```

Lo cual se obtendría:

```
https://download[Irrelevante].mediafire.com/[Irrelevante]/[Irrelevante]/[Nombre del archivo].[Extensión]
```

**Obtener enlaces de una carpeta:**

```bash
python3 mediafire2links.py d [Identificador]
```

Suponiendo que **[*Identificador*]** sea '**365frs9t3jqna**', entonces la URL se vería más o menos así:

```
https://www.mediafire.com/folder/365frs9t3jqna
```

El resultado puede ser algo como:

```
https://download[Irrelevante].mediafire.com/[Irrelevante]/[Irrelevante]/[Nombre del archivo #1].[Extensión]
https://download[Irrelevante].mediafire.com/[Irrelevante]/[Irrelevante]/[Nombre del archivo #2].[Extensión]
https://download[Irrelevante].mediafire.com/[Irrelevante]/[Irrelevante]/[Nombre del archivo #3].[Extensión]
```

**Nota**: Todo lo que diga **[*Irrelevante*]** es para evitar colocar información que podría resultar perjudicial.

# Experimental

El script es experimental, cualquier colaboración es bienvenida.

\~ DtxdF
