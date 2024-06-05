# Proyecto Urban Grocers 
## API Urban Grocers
Urban Grocers es un aplicacion desarrollada para la creacion de kits personalizados y realizacion de pedidos de productos comestibl es,los cuales son enviados a travez de un gestion de ordenesu envios,administrados por almacenes especificos.
Estas acciones son ejecutadas a atraves de solicitudes especificas hechas para cada opcion.
Este proyecto se trata de la ejecución de pruebas a la solicitud de creacion de un kit para un usuario creado, especificamente del campo "name"y sus condiciones y limitaciones

# Programas Instalados

- Las herramienta:
-Pycharm
-Git Bash
-Git Hub Destokp
- Paquetes dentro del Pycharm:
-Pip Request
-Pip Pytest
- Lenguaje de programacio:
Python

# Objetivos de los archivos
El proyecto consta de 6 archivos fundamentales
- .gitignore: 
- README.md: Posee documentacion y una descripción informativa sobre el proyecto
- configuration.py: Archivo utilizado para el almacenamiento de las rutas
- data.py: Utilizado para la crecion de diccionarios sobre el cuerpo y encabezado de la solitud kit y nombramiento de la variable kit_body
- sender_stand_request.py: Archivo utilizado para la importacion de los archivos (configuration y data) y el paquete de request, la definicion de las funciones necesarias para la creacion del usuario y su token, y de la creacion del kit.
- create_kit_name_kit_test.py: Finalmente, este archivo es empleado para la importacion del archivo sender_stand_request y data; y las definiciones de un total de 9 pruebas entre ellas; negativas y positivas, de rangos limites y caracterer permitidos sobre el parametro o campo "name" 

# Informacion relevante de la automatizacion

Es importante recordar que el serividor utilizado posee un tiempo de duracion, el cual se debe renovar en la variable "URL_SERVICE" nombrada en el archivo configuration.py

# Documentacion:
https://cnt-da0191a8-eea5-42cc-ac11-c4d8115d0e1e.containerhub.tripleten-services.com/docs/#api-Warehouses

