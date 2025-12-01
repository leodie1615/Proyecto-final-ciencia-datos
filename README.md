# Integrantes:
- 202512491 Ivan Suarez
- 202525657 Diego Baron
- 202523012 Santiago Palacios
- 202525326 Miguel Benavides


# Instalaciones
Para ejecutar el notebook proyecto_final_segunda_entrega.ipynb se debe ejecutar en consola cmd el comando ".\setup.bat", con el fin de instalar ambiente virtual y librerías necesarias para la ejecución del notebook. Luego, se debe seleccionar el kernel **venv** para ejecutar las celdas de código. Asimismo, el notebook utiliza como insumo principal para el entrenamiento del modelo la base maestra_segunda_entrega.rar. Este archivo debe ser descomprimido previamente para obtener el archivo en formato .csv, el cual es requerido para cargar, explorar y procesar los datos durante el desarrollo del modelo.

Para el despliegue y consumo del modelo, se debe correr en consola los siguientes comandos:
- pip install scikit-learn  (una sola vez)
- pip install streamlit     (una sola vez)
- pip install joblib        (una sola vez)
- python -m streamlit run app_2.py


Una vez ejecutados los comandos, se abrirá en el navegador la interfaz de Streamlit. Allí, el usuario deberá ingresar las características del proyecto a estimar, y la aplicación utilizará el modelo cargado para generar y mostrar la estimación de duración en horas.

**Instalación de datos primera entrega :** El dataset de Gryzzly requerido para el análisis puede ser ubicado en el siguiente enlace: [Repositorio de Datos](https://figshare.com/articles/dataset/Screenshot_2024-12-23_at_11_02_48_png/28114247/2). Es necesario descargar los archivos .csv que se encuentran en el dataset y guardarlos en la carpeta /data una vez se haya clonado el presente repositorio.

# Proyecto Ciencia de Datos
El propósito de este proyecto es aplicar el conjunto de técnicas y herramientas vistas durante el semestre para desarrollar un proyecto de ciencia de datos en una organización.

<p align="justify">
Con la intención de realizar una entrega de acuerdo a lo propuesto en el enunciado del proyecto académico, parte del contenido se desarrollará en el presente README. El PDF entregable solo es un resumen ejecutivo con la información más relevante. 


# Entregables
<p align="justify">
El presente repositorio contiene todos los archivos necesarios para el desarrollo y el entendimiento del proyecto. A continuación se listan algunos de los archivos relevantes:  
 
 - ETL_V0.1.ipynb: notebook complementario utilizado para recolectar información de los correos de la empresa.
 
 - proyecto_final_entrega_dos.ipynb:  notebook utilizado para recolectar la información del dataset. Es el principal objeto de análisis y donde se encuentra la solución del proyecto.

 - API_IMG.zip: Archivo comprimido que contiene el código relacionado con el API. Para ejecutar se debe usar archivo app.py

 - dashboard_IMG.zip: Archivo comprimido que contiene los archivos de datos y el archivo que contiene el dashboard

 - Presentación Entrega: presentación de PowerPoint que es material de la sustentación. El video de la presentación puede ser encontrado en el siguiente enlace: [Video Sustentacion](https://youtu.be/EOA7mniwaAU)

 - Resumen Ejecutivo: archivo pdf que contiene el resumen ejecutivo de la entrega del proyecto.
 
---


# Entrega 1

## 1. Problemática y Negocio.

 ![Proyecto Logo](media/logo_img.jpg)

<p align="justify">
La empresa analizada es IMG Procesos y Tecnología, ubicada en Bogotá, Colombia, con más de 15 años de experiencia en el desarrollo de soluciones orientadas a la centralización, gestión y disponibilidad de la información para sus clientes. 

<p align="justify">
Su foco está en la implementación de soluciones de software que mejoren la productividad, la trazabilidad y la toma de decisiones. Actualmente, los colaboradores (especialmente los desarrolladores)  deben diligenciar un formato para registrar las actividades de los proyectos en los que participan. Esta práctica fragmentada impide la consolidación de la información en un repositorio centralizado, dificultando el seguimiento oportuno, la trazabilidad de las tareas y la medición real de la productividad.
 
<p align="justify">
El principal problema radica en esta falta de integración con el repositorio centralizado, lo que impide contar con un sistema eficiente de time & activity tracking, el cual a su vez limita la visibilidad sobre la gestión de los empleados y restringe la capacidad de análisis y optimización de los procesos internos de la compañía. 

<p align="justify">
Como consecuencia directa, la organización enfrenta limitaciones significativas en la gestión de sus proyectos y del talento humano. En primer lugar, la falta de un control preciso entre los costos reales y los costos planificados dificulta la toma de decisiones presupuestales y la evaluación de la rentabilidad de los proyectos. En segundo lugar, la ausencia de datos consolidados impide un análisis objetivo del desempeño de los colaboradores, ya que no se cuenta con información confiable sobre el tiempo invertido, las tareas ejecutadas o los niveles de productividad individual y colectiva. 

<p align="justify">
Por último, la falta de integración de la información en un repositorio centralizado limita el acceso a métricas clave de desempeño en tiempo real, como el avance porcentual de los proyectos, la eficiencia operativa o el grado de cumplimiento de los objetivos. Esta situación afecta de manera directa la capacidad de la empresa para realizar un seguimiento continuo, anticiparse a desviaciones y aplicar estrategias correctivas de forma oportuna. 

**Objetivo General**
<p align="justify">
 Diseñar e implementar una solución integral de registro, integración y análisis de datos que permita optimizar la trazabilidad, productividad y gestión de los proyectos en IMG Procesos y Tecnología, facilitando la toma de decisiones basadas en información confiable y en tiempo real.

**Objetivos Especificos**

- Centralizar la información de registro de actividades de los empleados en un repositorio único y estructurado.
- Automatizar y estandarizar el proceso de captura de datos mediante una API transaccional y una interfaz de usuario intuitiva.
- Desarrollar un dashboard analítico que integre métricas de desempeño de proyectos, costos y productividad del talento humano.
- Mejorar la visibilidad y control sobre la ejecución de proyectos mediante indicadores.
- Fortalecer la toma de decisiones estratégicas basadas en evidencia, mediante reportes e indicadores.


**Definición de KPIs**


| KPI | Descripción | Fórmula / Método | Propósito |
|---|---|---:|---|
| **Porcentaje de proyectos en riesgo** | Mide la proporción de proyectos que presentan desviaciones superiores al 20% en tiempo o costo. | `(Proyectos con desviación > 20% / Total proyectos) × 100` | Detectar proyectos críticos y anticipar acciones correctivas.|
| **Cumplimiento horas proyectos (%)** | Compara las horas reales con las horas presupuestadas en proyectos. | `(Horas planificadas / Horas reales) × 100` | Controlar sobrecostos y rentabilidad de proyectos.|
| **Cumplimiento horas tareas (%)** | Horas reales vs. horas presupuestadas por tarea. | `(Horas planificadas / Horas reales) × 100` | Controlar sobrecostos y rentabilidad de tareas. |
| **Porcentaje de avance promedio por proyecto** | Progreso reportado sobre tareas planificadas. | `(Tareas completadas / Tareas totales) × 100` | Medir avance general y la adherencia al plan. |
| **Productividad promedio por empleado (horas/tarea)** | Mide el tiempo promedio que tarda cada colaborador en completar una tarea . | `Total horas registradas / Total tareas completadas` | Comparar desempeño y detectar cuellos de botella. |


## 2. Ideación
<p align="justify">
Para dar respuesta a la problemática identificada, se propone el diseño e implementación de una solución integral basada en datos, orientada a optimizar la trazabilidad, el control y la toma de decisiones sobre la gestión de proyectos y del talento humano. La iniciativa contempla el desarrollo de tres productos de datos interconectados que permitan transformar la información operativa dispersa en conocimiento estratégico y accionable.


<p align="justify">
<strong>Integración de datos (ETL)</strong>:  El primer paso consiste en centralizar toda la información proveniente de los formularios de registro de actividades de los empleados en un repositorio unificado. Esta integración permitirá eliminar la dependencia de canales informales como el correo electrónico y garantizar la disponibilidad, consistencia y trazabilidad de los datos. De esta manera, la empresa contará con una fuente única de información confiable que facilite los análisis transversales por proyecto, área o colaborador
 
 <p align="justify">
<strong>API de registro de actividades</strong>: El segundo componente corresponde al desarrollo de una API transaccional, acompañada de una interfaz gráfica amigable, que reemplace los formatos manuales actuales. A través de esta herramienta, los empleados podrán registrar sus actividades en tiempo real, asignarlas a proyectos específicos y enviar automáticamente la información al repositorio de datos. Este flujo digitalizado reducirá errores humanos, estandarizará los procesos de captura y habilitará un ecosistema de datos más accesible, escalable y gobernable.

 <p align="justify">
<strong>Dashboard de gestión y desempeño</strong>: Finalmente, se propone la creación de un tablero interactivo de control y seguimiento, orientado a la analítica de proyectos y productividad. Este dashboard permitirá visualizar los costos planificados versus los reales, el avance de tareas por empleado o equipo, y los principales indicadores de rendimiento, eficiencia y cumplimiento de objetivos. El tablero consolidará métricas a distintos niveles de agregación (diario, semanal, quincenal y mensual), facilitando el monitoreo de tendencias y la toma de decisiones basadas en evidencias.

 <p align="justify">
<strong>Modelo de Analitica</strong>:  Por sugerencia del personal docente y con la intención de completar más ampliamente el alcance del proyecto se implementa también la creación de un modelo de Machine Learning. Para los datos de entrenamiento se hará uso de un dataset externo con características similares a las estructuras de datos de la empresa IMG, el objetivo es que en un futuro cercano el modelo pueda ser ajustado a las necesidades de la empresa usando sus propios registros.


A continuación, se presenta los requerimientos funcionales y no funcionales para cada uno de los productos de datos:


### ETL (Integración de Datos)

**Requerimientos funcionales**
- **Centralización de datos:** La ETL debe integrar en un único repositorio toda la información proveniente de los formularios de registro de actividades de los empleados, sin importar su origen 
- **Estandarización de formatos:** El sistema debe transformar los datos heterogéneos en un formato uniforme y estructurado
- **Validación de calidad de datos:** La ETL debe incluir reglas automáticas de validación que detecten registros incompletos, duplicados
- **Control de trazabilidad:** Se debe registrar metadatos de cada carga (fecha de extracción, origen de los datos, usuario responsable, número de registros) para asegurar la trazabilidad completa del flujo.
- **Actualización programada y/o incremental:** La ETL debe ejecutar cargas incrementales permitiendo la actualización para evitar reprocesar la totalidad del histórico cada vez.
- **Integración con repositorio centralizado:** La salida del proceso ETL debe almacenarse en un data warehouse o data lake corporativo, donde los analistas puedan consultar información unificada por proyecto, colaborador o periodo.

**Requerimientos no funcionales**
- **Calidad e integridad:** Los datos cargados al repositorio deben ser completos, consistentes y sin duplicados, asegurando la confiabilidad de los análisis y reportes.
- **Disponibilidad:** La plataforma de integración debe garantizar una disponibilidad mínima del 99.5%
- **Escalabilidad:** El sistema debe poder procesar volúmenes crecientes de datos (más proyectos, empleados y tareas) sin pérdida significativa de rendimiento.
- **Rendimiento:** El tiempo total de procesamiento por lote (extracción, transformación y carga) no debe exceder los 30 minutos para datasets de tamaño estándar (por ejemplo, 100k registros).

### API de registro de Actividades

**Requerimientos funcionales**

- **Registro de actividades:** La API debe permitir que los empleados registren sus actividades directamente desde una interfaz web, capturando información como: tarea, proyecto asociado, fecha, hora de inicio y fin, y descripción de la actividad.
- **Asignación a proyectos y colaboradores:** Cada registro debe asociarse de forma automática a un proyecto y a un colaborador, validando que ambos existan en el sistema y estén activos.
 - **Validación de datos de entrada:** La API debe incluir reglas de validación para evitar errores comunes (por ejemplo, tiempo negativo, campos vacíos, fechas futuras o proyectos inexistentes).
 - **Sincronización con el repositorio central:** Una vez registrada la actividad, la API debe enviar los datos de forma automática e inmediata al repositorio central (data warehouse o data lake), garantizando la consistencia entre los sistemas.
 - **Control de acceso:** El sistema debe requerir acceso de usuario y asignar permisos según el rol (empleado, líder de proyecto, administrador).
 - **Consulta y edición de registros:** Los empleados deben poder consultar, actualizar o eliminar sus registros recientes (según políticas definidas), mientras los administradores pueden gestionar todos los registros.
 - **Interfaz gráfica amigable:** Debe desarrollarse una interfaz intuitiva que facilite la carga de información, priorizando la usabilidad y la reducción de errores humanos.
 - **Compatibilidad con otros módulos:** La API debe integrarse de forma nativa con el Dashboard de gestión y desempeño, facilitando el flujo completo de datos en el ecosistema.

**Requerimientos no funcionales**
- **Disponibilidad:** El servicio debe garantizar un 99.9% de disponibilidad, permitiendo que los usuarios registren actividades en cualquier momento, incluso en horarios no laborales.
- **Escalabilidad:** La API debe poder manejar un aumento en el número de solicitudes concurrentes (por ejemplo, en cierres de mes) sin afectar el rendimiento.
- **Baja latencia:** El tiempo máximo de respuesta para el registro o consulta de actividades no debe superar los 10 segundos en condiciones normales de carga.

### Dashboard de control

**Requerimientos funcionales**
- **Visualización de KPIs:** El dashboard debe mostrar métricas sobre la productividad, cumplimiento de tiempos, y avance de los proyectos, tanto a nivel individual como colectivo.
- **Comparativo planificado vs. real:** Debe incluir gráficos y tablas que permitan comparar las horas planeadas y horas reales de los proyectos, así como el porcentaje de cumplimiento y desviación.
- **Niveles de agregación:** El sistema debe permitir visualizar los indicadores de gestión a distintos niveles de granularidad (diario, semanal, quincenal y mensual), facilitando el monitoreo de tendencias.
- **Filtros dinámicos:** Los usuarios deben poder filtrar la información por variables como: empleado, proyecto, equipo, o estado del proyecto (en curso, finalizado, exitoso, retrasado).
- **Actualización automática:** Los datos deben actualizarse de forma automática a partir del repositorio centralizado.
- **Exportación y reportes automáticos:** El sistema debe permitir exportar reportes en formatos estándar (PDF, Excel, CSV) y generar informes automáticos para líderes de proyecto o directivos.
- **Interfaz interactiva:** El dashboard debe contar con una interfaz gráfica, permitiendo una rápida interpretación de la información a través de gráficos, tarjetas y paneles comparativos

**Requerimientos no funcionales**
- **Disponibilidad:** El tablero debe garantizar una disponibilidad mínima del 99.5%, permitiendo la consulta continua por parte de los usuarios.
- **Rendimiento:** Los tiempos de carga y actualización de los visuales no deben superar los 10 segundos en condiciones normales.
- **Escalabilidad:** El sistema debe ser capaz de soportar un aumento en la cantidad de proyectos, empleados o registros sin degradar el rendimiento general.
- **Seguridad:** Los datos sensibles (por ejemplo, costos y desempeño individual) deben cifrarse o restringirse por nivel jerárquico.
- **Integridad:** Todos los indicadores deben basarse en datos provenientes del repositorio central, asegurando consistencia y trazabilidad.
- **Compatibilidad tecnológica:**  Debe desarrollarse utilizando herramientas analíticas y de visualización modernas y compatibles con la infraestructura existente (por ejemplo, Power BI, Tableau o Looker Studio).


### Mockups
![Mockup Dashboard](media/mockup_dashboard.jpg)

![Mockup API](media/mockup_api.jpg)

## 3. Responsible
<p align="justify">
Teniendo en cuenta que la información recopilada a través de los productos mencionados previamente se caracteriza por ser de carácter corporativo y operativo, no se identifica riesgo asociado a la presencia de datos personales de trabajadores en esta información, por lo que las directrices estipuladas a través de la Ley 1581 de 2012 (Congreso de Colombia, 2012) para la protección de datos personales no tiene lugar en el marco regulatorio del proyecto. A pesar de esto, se debe priorizar los derechos laborales de los trabajadores, salvaguardando la integridad de información corporativa, llevando a que sea necesario la aplicación de principios de seguridad, confidencialidad y proporcionalidad.

<p align="justify">
En materia de transparencia, se encontró necesario el desarrollo de un canal de comunicación abierto y continuo que permita conocer el propósito del sistema, datos que se procesan y beneficios esperados promoviendo de esta manera una cultura de confianza. Es indispensable que sea claro que los reportes se emplearán únicamente para consolidación de métricas operativas, trazabilidad de costos operacionales e identificación de puntos de mejora.

<p align="justify">
Lo anterior lleva a evaluar la ética necesaria para el desarrollo del proyecto, considerando la responsabilidad social necesaria para que el proyecto mantenga su foco de fortalecimiento de productividad y se mantenga alejado de un control individual. Para esto, se considera imprescindible la implementación de una política interna de tratamiento de datos no personales. El objetivo de esta política de datos organizacional es que las decisiones tomadas a partir de la información recolectada sean justa, informada y respetuosas en el contexto humano, centrándose en la optimización de procesos operacionales y no en prácticas que puedan llevar a acoso laboral (Banco Interamericano de Desarrollo, 2019).
<p align="justify">
Finalmente, aunque no se identifique presencia de datos personales, se encontró un potencial riesgo en el manejo de información confidencial para la compañía, referente a tareas, clientes y presupuestos de proyectos. En los productos de datos planteados se debe garantiza que esta información, de gran valor para la compañía, se mantenga al alcance de personal autorizado. (ESEID, 2024)


## 4. Enfoque Analítico
**Hipótesis nula (H0):**  
> *No hay diferencia en el uso de recursos (horas, presupuesto) entre proyectos que usan una herramienta de monitoreo diario y los que no.*

<p align="justify">
Para el presente experimento la hipótesis nula plantea que el efecto de una herramienta de control sobre los proyectos es inexistente, es decir que el monitoreo constante no afecta al uso de los recursos en los proyectos. Esto probablemente conduzca a una hipótesis alternativa como la siguiente:


**Hipótesis alternativa (H1):**  
> *Si hay diferencia en el uso de los recursos (horas de trabajo, presupuesto) entre los proyectos que utilizan una herramienta de monitoreo diario y los que no*

<p align="justify">
La hipótesis alternativa sugiere que una herramienta de control sobre los proyectos si tiene un impacto sobre el uso recursos, es decir que el monitoreo constante afecta en cierta medida en los proyectos. Es incluso posible para el caso particular generar más hipótesis de mayor complejidad a ser evaluadas en el experimento, con ideas orientadas a probar a la dirección del impacto “La herramienta de monitoreo disminuye el uso de recursos” o con hipótesis orientadas al tipo de recurso impactado “La herramienta de monitoreo aumenta el uso de horas de trabajo en los proyectos”.

<p align="justify">
Para las técnicas estadística se propone por ejemplo un T-Test para comparar el desempeño de un proyecto donde no se haya realizado monitoreo con las nuevas herramientas comparado contra un proyecto si se haya realizado monitoreo constante.  El enfoque principal del proyecto de datos está en la disponibilización y visualización de los datos que actualmente no están congregados. Por lo tanto, se sugieren las siguientes técnicas de visualización para el dashboard:  

<p align="justify">
<strong>Para el KPI de Porcentaje de avance por proyecto:</strong> se sugiere una grafico de barras horizontales donde cada barra sea un proyecto, la longitud es el porcentaje de avance y se utiliza una codificación de colores (rojo, amarillo, verde)

<p align="justify">
<strong>Para el KPI de Cumplimiento de horas por tarea o proyecto:</strong> se sugiere un gráfico de dispersión donde el eje X sean las horas planificadas y el eje Y sean las horas reales. Se traza una diagonal y=x que indica un cumplimiento del 100% entre lo estimado y lo real. De esta manera los puntos que estén por encima de la diagonal están sobrestimando las horas de trabajo y aquellos que estén por debajo están subestimando. Se pueden adicionar también códigos de color para empleados o equipos.  

Para la hipotesis prácticas se propone:
**Hipótesis nula (H0):**  
> *Eficiencia promedio del empleado en proyectos exitosos es igual a la eficiencia promedio del empleado en proyectos no exitosos*

**Hipótesis alternativa (H1):**  
> *Eficiencia promedio del empleado en proyectos exitosos es diferente a la eficiencia promedio del empleado en proyectos no exitosos*

## 5. Recolección de Datos 
Para el presente proyecto se utilizan 2 fuentes de datos principales. 

<p align="justify">
<strong> Información de la empresa:</strong> Actualmente, el principal método para que las personas de la empresa registren las horas de trabajo es mediante correos que se envían diariamente al final de la jornada laboral. Adicionalmente, se recopila información proveniente de archivos de Excel que contienen los datos de los proyectos, las tareas y los empleados. La información de estas fuentes se recopila mediante notebooks o proceso manuales no incluidos en la presente entrega.  

<p align="justify">
Los correos que envían los empleados en la empresa contienen información relevante para el análisis del tiempo y la productividad: Fecha del registro, empleado, Id de la tarea realizada, horas trabajadas, horas estimadas, estado de la tarea, proyecto asociado. Estos correos tienen un formato de Timecard, y hacen parte fundamental de la estructura cultural de la empresa y de su estrategia de gestión de proyectos. Es funcional pero esencialmente rudimentario. 

<p align="justify">
Por otro lado, la información de los archivos de Excel contiene información estructural que complementa y contextualiza los registros horarios de los correos con: Proyectos (presupuestos, categoría, cliente asociado, fecha de inicio y fin.) Actividades (Proyecto asociado, presupuesto, categoría, fecha de inicio y fin). Tareas y Subtareas (Actividad asociada, horas presupuestadas, fecha de inicio y fin.), además, información básica de los empleados y los clientes.

<p align="justify">
<strong> Dataset de Grizzly:</strong> Por sugerencia del personal docente del presente proyecto académico y frente a la relativa baja de cantidad de datos presentes en la empresa se incluye datos de un dataset abierto que comparte características similares con la estructura de datos de la empresa. El objetivo es que el presente Dataset permita realizar análisis más complejos y experimentar más escenarios en el ejercicio académico, como por ejemplo entrenar un modelo o visualizar volúmenes de datos en un dashboard.  Es importante aclarar que la información del Dataset no será incluida en el entregable a la empresa

<p align="justify">
El conjunto de datos utilizado contiene información detallada sobre tareas, proyectos y equipos registrados en la plataforma Gryzzly, orientada al seguimiento del tiempo y desempeño de los proyectos. Entre sus campos principales se encuentran: los identificadores de tarea (tarea_id) y proyecto (proyecto_id), las fechas de creación (creacion_tarea_grizzly, creacion_proyecto_grizzly), la duración planeada y real de cada tarea y proyecto (duracion_total_planeada_tarea, duracion_real_total_tarea, duracion_total_planeada_projecto, duracion_real_total_projecto), así como la fuente de registro (fuente) y el estado del equipo o empresa (estado, oferta). Adicionalmente, se incluye información temporal sobre los equipos (creacion_team_grizzly, eliminacion_team_grizzly, duracion_meses_team), así como también la fecha donde el usuario registró la tarea en Grizzly (fecha_registro_grizzly_empleado), como también la fecha cuando realizó dicha tarea el empleado (fecha_tarea_empleado). 

Para más información sobre el Dataset de Grizzly, se puede acceder al siguiente enlace:   [Seven years of time-tracking data capturing collaboration and failure dynamics: the Gryzzly dataset](https://www.nature.com/articles/s41597-025-04903-2#)

**Diagrama de Recolección de Datos** 
<p align="justify">
El siguiente diagrama resume el flujo de origen y consumo de los datos utilizados en el proyecto. Del lado izquierdo, la información interna de la empresa es recolectada para crear un dashboard de Monitoreo. Inicialmente los datos históricos se recolectan con una ETL, encargada de extraer la información existente en los correos corporativos y los archivos de Excel. 

![Estructura de Datos](media/estructura_datos.jpeg) 

<p align="justify">
A futuro los empleados usarán un API donde podrán hacer el registro de sus horas y crear entidades como tareas, o proyectos, eliminando la dependencia de los correos y ciertos archivos más tradicionales.  

<p align="justify">
En el lado derecho de la gráfica, se presenta la fuente de datos externa, el dataset de Grizzly, el cual se emplea exclusivamente con fines académicos para la experimentación analítica y el desarrollo de un modelo de Machine Learning. Este dataset no se integrará al entregable empresarial ni se mezclará con los datos reales de IMG. 


**Sobre la compatibilidad de Grizzly** 
<p align="justify">
La inclusión de un dataset abierto que apoyara el ejercicio académico en el proyecto era completamente necesario debido a la baja cantidad de datos presentes en la empresa. Tras una investigación de parte de los estudiantes se selecciona el dataset Grizzly dado que tiene una estructura muy similar a la de IMG en sus datos. También tiene un contexto similar pues se trata de una recolección de timecards en proyectos de software en industrias de Marketing, Finanzas y Bancos, además de haber sido publicado en abril de 2025 y contener información de los últimos años (2017-2024).  

 <p align="justify">
Es cierto que existen diferencias contextuales, por ejemplo, el país. Los datos del Grizzly provienen de Francia, mientras que la empresa IMG en su contexto colombiano tendrá diferencias clave como la inexistencia de estaciones que afecten las horas trabajadas. A pesar de estas diferencias se define que Grizzly es la mejor opción para crear un modelo de analítica que luego pueda ser ajustado y modificado para las necesidades de IMG, una vez exista un volumen de datos suficiente.  

## 6. Entendimiento de los Datos
<p align="justify">
El procedimiento del entendimiento de los datos junto a todo el procesamiento técnico de los mismos se realiza en el notebook de Python llamado “proyecto_final.ipynb” ubicado en este mismo repositorio.
<p align="justify">
Como se indicó anteriormente, el presente proyecto cuenta con dos fuentes de datos principales; el Entendimiento de los Datos se realiza sobre el Dataset de Grizzly, pues esto habilita los datos para su uso posterior en la creación del Modelo de Analitica. 

## 7. Conclusiones Iniciales
<p align="justify">
El registro de horas en la empresa presenta actualmente una alta dispersión de la información entre correos electrónicos y archivos de Excel. Centralizar los registros de las actividades representa un paso inicial para visualizar y disponibilizar la información y aproximarse a un mejor gobierno de datos.
 
<p align="justify">
Los productos de Datos presentados (API, Dashboard, ETL) responden a necesidades existentes en la organización y permiten un futuro con mayor control, además de habilitar la toma de decisiones basada en datos. Se espera que el monitoreo diario reduzca desviaciones de tiempo, sobrecostos y errores de estimación. El cumplimiento de horas y la productividad podrían aumentar en los diferentes equipos y proyectos trabajados.
 
<p align="justify">
En la siguiente etapa, se espera enfocarse en terminar el desarrollo y completar la entrega de los productos de datos a la empresa, para que puedan ser implementados y usados, y así, comiencen a proveer valor real para la organización  

### 7.1 Insights
<p align="justify">
Con base a la hipotesis practica planteada en donde se comprobo que en los proyectos exitosos los empleados son mas eficientes, se propone implementar las siguientes estrategías:
 
Identificación y difusión de buenas prácticas
<p align="justify">
→ Analizar el comportamiento y métodos de los empleados más eficientes para documentar y replicar sus buenas prácticas en el resto del equipo (p. ej., gestión del tiempo, priorización de tareas, enfoque técnico).

Fortalecimiento del proceso de planeación y control
<p align="justify">
→ Implementar mecanismos para mejorar la estimación de tiempos y realizar monitoreo temprano de desviaciones entre horas planeadas y reales, con alertas para corregir errores de planificación o problemas de coordinación.

Diseño de incentivos basados en eficiencia y cumplimiento
<p align="justify">
→ Crear políticas de reconocimiento o recompensas enfocadas en la eficiencia sostenida (cumplimiento de planes y calidad del trabajo), no solo en la cantidad de horas trabajadas.

## 8. Preparación de datos
<p align="justify">
Como insumo se utilizó la base transformada de la primera entrega (datos recolectados de la plataforma Grizzly). Las métricas del modelo mejoraron significativamente gracias a un conjunto de transformaciones de limpieza y enriquecimiento de los datos, que permitieron reducir el ruido, elevar la calidad de las variables y mitigar el impacto de valores extremos que afectaban el aprendizaje. En particular:  

- Creación de variables agregadas como cantidad_tareas y num_seguimientos, orientadas a capturar la intensidad operativa de cada proyecto mediante conteos consolidados.  

- Tratamiento de la asimetría en variables numéricas, donde se identificó una asimetría positiva elevada. Se aplicó winsorización basada en criterios del negocio, reduciendo la influencia de outliers sin eliminar información relevante. Esta corrección contribuyó a disminuir el RMSE.  

- Depuración de valores atípicos en la variable objetivo (duracion_real_total_projecto), seleccionando rangos representativos de los proyectos con mayor frecuencia para mejorar la estabilidad del modelo.  

- Imputación de valores faltantes en la variable duracion_meses_team, reemplazando nulos por el promedio para preservar coherencia en el comportamiento histórico.  

- Codificación de variables categóricas mediante OneHotEncoder, adecuado dado que estas columnas no presentaban alta cardinalidad. 

- Estandarización de variables numéricas utilizando StandardScaler, para homogenizar escalas y favorecer el desempeño de modelos sensibles a magnitud. 

## 9. Estrategia de validación y selección de modelo
<p align="justify">
Se implementó una estrategia de validación robusta combinando una división inicial de los datos en entrenamiento y prueba (80%-20%, con random_state=42) junto con un proceso de búsqueda de hiperparámetros mediante GridSearchCV. Aunque se mantiene un conjunto de prueba independiente para la evaluación final, GridSearchCV aplica validación cruzada interna, dividiendo automáticamente el conjunto de entrenamiento en n folds. En cada iteración, el modelo entrena en una fracción de los datos y valida en la restante, rotando los folds. Este procedimiento reduce el riesgo de sesgo por particiones aleatorias y permite seleccionar el modelo e hiperparámetros óptimos de forma más confiable. Así, la evaluación final se realiza únicamente sobre el conjunto de prueba, garantizando imparcialidad en la medición del desempeño.   


## 10. Construcción y evaluación del modelo
El objetivo del modelo es predecir la duración real (en horas) de los proyectos. Para ello se entrenaron y evaluaron tres algoritmos distintos: LinearRegression, RandomForestRegressor y XGBRegressor, cada uno explorado mediante diferentes configuraciones de hiperparámetros con el fin de identificar la mejor versión de cada modelo.  

Se implementó un proceso sistemático de experimentación donde se definieron grillas de hiperparámetros para Random Forest y XGBoost, utilizando validación cruzada para seleccionar los modelos con mejor desempeño según las métricas definidas en el enfoque analítico (MAE, RMSE y R²). En contraste, LinearRegression se evaluó como un modelo base para establecer un punto de referencia.  

Los resultados muestran que RandomForestRegressor y XGBRegressor presentan desempeños muy similares en términos de R², ambos significativamente superiores al modelo lineal. El modelo de regresión lineal obtiene valores de R² aproximadamente 10 puntos porcentuales por debajo, lo cual evidencia que las relaciones entre las variables y la variable objetivo no son puramente lineales. En cambio, los modelos basados en árboles capturan de manera más efectiva patrones no lineales y efectos de interacción presentes en los datos.  

En términos de oportunidades de mejora, se identifican posibles líneas de trabajo futuras como: incorporar nuevas variables derivadas que capturen relaciones no lineales, evaluar modelos polinómicos o modelos de ensamble más complejos, y profundizar en el manejo de valores atípicos para reducir aún más el error de predicción. 

| Modelo | MAE | RMSE | R2 |
|---|---|---:|---|
| **LinearRegression** | 3.85 | 4.98 | 0.47 |
| **RandomForestRegressor** | 3.35 | 4.00 | 0.57 |
| **XGBRegressor** | 3.29 | 4.98 | 0.57 |

Por otro lado, la métrica principal seleccionada para la evaluación fue el MAE, dado que proporciona una interpretación directa del error promedio en horas entre la duración predicha y la duración real del proyecto. Los resultados muestran que, para los tres modelos evaluados, el MAE se encuentra en un rango entre 3.2 y 3.8 horas, lo cual indica un nivel de error relativamente estable y comparable entre los modelos, con ligeras ventajas para los modelos basados en árboles sobre la regresión lineal.  

En un contexto empresarial, un R² del 57% no es perfecto, pero sí útil y accionable, especialmente si la organización no es todavía data-driven y apenas comienza a integrar modelos predictivos. Permite generar estimaciones más informadas que la intuición o que reglas manuales, y sirve como base para seguir mejorando el proceso de modelado y recolección de datos. 



## 11. Construcción del Producto de Datos
A continuación, se describen los productos de Datos entregables en el presente proyecto a partir de la ideación inicial, para cada uno se da una descripción inicial, su método de despliegue y los archivos entregables relacionados en el repositorio.  

### ETL 
<p align="justify">
El flujo de la ETL tiene como propósito recolectar y consolidar los datos históricos provenientes de los correos de registro de horas y de los archivos de Excel utilizados por la empresa. Dado que el registro actual se realiza mediante correos diarios con formato de timecard, el ETL se encarga de la lectura, limpieza y recolección. Se implementó mediante un script en Python que recorre una carpeta con los correos descargados, extrae los campos relevantes y los transforma en un archivo CSV estructurado. 

 - **Despliegue:** La ETL se ejecuta únicamente una vez para cargar el histórico inicial al repositorio de datos. Posteriormente, la recolección de información será reemplazada por la API, por lo que el ETL no hace parte del proceso operativo futuro. El script puede ejecutarse en cualquier directorio local o servidor interno de la empresa, sin requerir infraestructura adicional. Por último, el ETL será entregado a la empresa como una herramienta para ejecutar cuando se comience la implementación de la API.
 - **Archivo entregable:** Se entrega el script en Python, el archivo CSV resultante del procesamiento. Ubicado en el repositorio bajo ETL_V0.1.ipynb 


### API REST 
<p align="justify">
La API representa la estrategia principal para la recolección de datos en el futuro. Permite registrar horas de trabajo, crear tareas y proyectos, actualizar estados y consultar información de forma estructurada y centralizada. Inicialmente la API se alimenta de la información recolectada por la ETL usando los registros históricos, asegurando que estos sean almacenados. Mediante el futuro uso por las personas de la empresa, la API habilita la trazabilidad, estandarización y validación de los datos ingresados.  
<p align="justify">
La API se implementó usando Python y las librerías de Flask y SQLAlchemy. Como base de datos se usa un archivo .db llamado trazabilidad, a futuro podría establecerse una base de datos transaccional que se aloje en un servidor.  

- **Despliegue:** El despliegue del API se realizará mediante la intranet de la empresa IMG Procesos y Tecnología. Solo es necesario permitir acceso a usuarios autorizados que se encuentren dentro de la red interna de la empresa.  
- **Archivo Entregable:** Se entrega todo el código fuente de la API junto a la base de datos. Esto incluye todas las pantallas (.html), junto con su lógica (.js) y su apariencia (.css). Para ejecutar la API se debe correr el script llamado app.py. Todos los documentos de la API se encuentran bajo el archivo API_IMG.zip  

### Dashboard 
<p align="justify"> 
El dashboard habilita el monitoreo de la operación de la empresa, la integración de KPIs claves como el avance de los proyectos, el cumplimiento de las horas o la productividad de los trabajadores y la detección temprana de posibles complicaciones. El dashboard se conecta directamente al repositorio administrado por la API, asegurando que la información esté centralizada, actualizada y de fácil acceso.  
<p align="justify">
El Dashboard se desarrolló utilizando Power BI, incluye 2 páginas con filtros y diferentes gráficas que permiten analizar la información del desempeño de los proyectos y los empleados. 

- **Despliegue:** El despliegue se realizará mediante una licencia de Power BI que habilite la publicación en línea. Se implementarán controles de accesos para asegurar que la información sea accesible solo por las personas del equipo administrativo.  
- **Archivo Entregable:** Se entrega el archivo .pbix que contiene las visualizaciones con el código DAX usado para calcular diferentes métricas. Además se adjunta la información de la base de datos como archivos .csv (para facilitar la instalación en la presente entrega). Todos los documentos del Dashboard se encuentran bajo el archivo: dashboard_IMG.zip  

### Modelo 
<p align="justify">
El modelo seleccionado para estimar la duración de los proyectos fue un algoritmo basado en árboles de decisión, elegido por su buen desempeño en tareas de predicción con datos heterogéneos. Este modelo utiliza como insumos variables como la duración planeada del proyecto, la cantidad de tareas asociadas, el número de seguimientos registrados y otras características relevantes que permiten capturar la complejidad y variabilidad de cada proyecto 

Propósito principal: validación rápida del funcionamiento, la experiencia de usuario (UX) y la lógica de preprocesamiento en un entorno de aplicación real. 

- **Despliegue:** Se implementó el despliegue del modelo predictivo de Machine Learning (el mejor modelo obtenido) por medio de la herramienta Streamlit. Esta fase se considera una Prueba de Concepto Funcional (PoC) con el siguiente alcance: 

- **Archivo entregable:** 
El entregable final consta de un conjunto de archivos (artefactos) que encapsulan el modelo entrenado y los transformadores de datos, junto con el script de la aplicación: 

- **Archivos entregables:**
  - `rf.joblib`: Modelo principal (encapsulado).
  - `standard_scaler.joblib`: Usado en `preprocess_and_predict` para escalar las variables numéricas de entrada.
  - `one_hot_encoder.joblib`: Usado en `preprocess_and_predict` para transformar las variables categóricas (como estado, oferta, fuente) en columnas binarias.
  - `final_columns.joblib`: Usado para asegurar que el DataFrame de entrada al modelo (`final_input_df`) tenga exactamente las mismas columnas y el mismo orden que se usó durante el entrenamiento.
  - `app_2.py`: Ejecutado con `streamlit run app_2.py` para lanzar el prototipo funcional.

#### Diagrama de arquitectura

A continuación, se presentan dos diagramas: 

![Arquitectura Proyecto](media/arquitectura.jpg) 

La arquitectura actual del presente proyecto, con los cuatro productos de datos que usan la fuente externa del dataset Grizzly y los datos internos de la empresa. El prototipo del Modelo de Analítica es un adicional para el ejercicio académico, pero no es integrado aun a la arquitectura empresarial 

![Arquitectura Proyecto](media/arquitectura_futuro.jpg) 

La arquitectura propuesta a futuro para la empresa, manteniendo los cuatro productos de datos, pero usando como principal fuente de información lo consignado por los usuarios mediante la API. La Base de Datos alimenta de datos al dashboard y al Modelo de Analítica, que ya está integrado en la solución empresarial y puede generar informacion adicional para los usuarios 



## 12. Retroalimentación por parte de la organización
Se realizaron varias reuniones con la IMG. La primera tuvo lugar el 26 de agosto de 2025 y tuvo como objetivo identificar las principales problemáticas que el producto buscaba resolver. Como resultado de esta sesión, se elaboró un mapa de empatía del cliente que permitió comprender sus necesidades y desafíos más relevantes. 

 ![Mapa Empatia](media/mapa_empatia.jpg) 

Una vez identificados los principales puntos de dolor de la organización, se diseñó el producto de datos en conjunto con el gerente administrativo de la compañía, definiendo el alcance esperado de dicho producto. Esta segunda reunión se realizó el 12 de septiembre de 2025. A partir de entonces, se sostuvieron múltiples encuentros de seguimiento para asegurar el avance del producto de datos y el cumplimiento de los objetivos establecidos. 

 ![Notas](media/notas.jpg) 

Finalmente, el 28 de noviembre de 2025 se realizó una entrega parcial de los productos de datos desarrollados en el proyecto. Durante esta entrega, se evidenció satisfacción por parte del cliente respecto al cumplimiento de los objetivos planteados. La organización manifestó conformidad tanto con el entorno de captura de información como con el entorno de visualización. No obstante, en etapa de pruebas funcionales, se identificaron algunos detalles menores relacionados con errores no controlados en el registro de datos, los cuales se espera corregir antes de la implementación definitiva de la herramienta en enero de 2026. 

## 13. Conclusiones 
¿Se cumplieron los objetivos del proyecto? 

Si, los objetivos propuestos inicialmente en el proyecto se cumplieron de manera satisfactoria. Se desarrollaron todos los productos de datos propuestos: la ETL inicial para consolidar la información histórica de la empresa, un API transaccional para la captura estructurada de la información, un dashboard que apoya el monitoreo y la gestión de proyecto, y un prototipo de modelo analítico. Todos estos productos permiten a IMG Procesos y Tecnología mejorar la trazabilidad, y el seguimiento de los proyectos, centralizar los datos, y facilitar la toma de decisiones basadas en datos 

- ¿Cuáles fueron las mayores dificultades que se obtuvieron durante su desarrollo 

El principal obstáculo está relacionado con la cantidad de datos encontrados en la empresa, después de haber comenzado el desarrollo del proyecto se encontró que el volumen de datos en IMG era insuficiente para la construcción de un Modelo de Analítica. Esta dificultad obligo a reformular el alcance técnico del proyecto, a incorporar un dataset externo y a tener esfuerzos adicionales con el entendimiento y procesamiento de los datos. A pesar de esto, el proyecto logro avanzar de manera apropiada, la inclusión de Grizzly permitió mantener el componente académico del curso y realizar procesos de analítica de datos, mientras que los demás entregables aportan valor a la estrategia de datos de la empresa. 

- ¿Qué estimación se puede dar respecto a cómo se impactarían las métricas de negocio (KPIs) una vez el producto de datos sea utilizado por usuarios reales? 

Tras la adopción de los productos de datos desarrollados, se espera que los KPIs del negocio vean un impacto en la optimización de costos operacionales, disminución de horas de desarrollo no estimadas, redistribución de personal en los equipos de trabajo, y trazabilidad de costos operacionales en los proyectos. De igual manera, se plantean impactos positivos en la centralización de la información y el registro de costos y presupuestos asociados a cada cliente. De manera estratégica, se preveen más casos de usos futuros producto de la centralización de la información que se desarrolla en estos productos de datos. 

- ¿Qué condiciones considera que deberían tener los datos para obtener mejores resultados? Más datos, nuevas características, menor sesgo, etc. 

La principal mejora para IMG sería un mayor volumen de datos disponibles de forma estructurada y centralizada, se espera que mediante la nueva API sea más sencillo para las personas de la empresa hacer sus registros diarios y de esta manera aumentar el histórico de datos, y así, ver tendencias y poder realizar analítica sobre los datos. Sería beneficioso también enriquecer las entidades actuales (Proyectos, Actividades, Tareas, Empleados) con atributos adicionales que aporten contexto, por ejemplo, categorías de trabajo, nivel de complejidad, nivel de prioridad, tipo de clientes, mantenimiento o nuevo desarrollo. Esta información adicional ampliaría las posibilidades analíticas de los modelos y permitiría crear nuevas métricas en el dashboard. En cuanto al dataset Grizzly, aunque su anonimización es comprensible, la ausencia de variables descriptivas (como categorías o nombres más interpretables) limitó parcialmente la comprensión del contexto. No obstante, su estructura permitió desarrollar escenarios analíticos útiles para el alcance académico del proyecto. 

- ¿El mejor modelo obtenido es suficiente para dar solución al problema u oportunidad de negocio abordado? 

Si bien el modelo no sustituye las necesidades de centralización y análisis operativo que ya cubren la aplicación web y el dashboard corporativo, sí aporta un valor adicional significativo frente a la problemática del negocio. La falta de control entre costos planificados y reales, la ausencia de datos consolidados para evaluar productividad y la imposibilidad de anticipar desviaciones afectan directamente la gestión de proyectos. En este contexto, el modelo desarrollado, que es capaz de predecir las horas reales de un proyecto a partir de información como horas planeadas, número de tareas y frecuencia de seguimiento, no resuelve por completo todas las brechas operativas, pero sí constituye un activo de datos útil y complementario. Su capacidad predictiva permite a los project managers estimar con mayor precisión el esfuerzo real requerido, anticipar desviaciones de costo y planificar proyectos con una base más informada, contribuyendo de forma tangible a la toma de decisiones y a la eficiencia organizacional.   
