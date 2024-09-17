# ECO_VISHIONAI

## Descripción General

ECO_VISHIONAI es una aplicación desarrollada con Python que utiliza un modelo YOLO (You Only Look Once) para la clasificación de objetos a partir de una cámara en tiempo real. La aplicación está diseñada para detectar cinco tipos diferentes de basura (metal, vidrio, plástico, cartón, y desechos médicos) y mostrar una interfaz gráfica utilizando la librería Tkinter.

Además de realizar la detección, la interfaz presenta al usuario imágenes ilustrativas que corresponden al tipo de basura detectada y textos explicativos para cada categoría, facilitando su clasificación.

## Requisitos del Sistema

- Sistema Operativo: macOS (M1), Windows o Linux
- Python: 3.8 o superior
- Librerías:
  - OpenCV
  - Tkinter
  - PIL (Pillow)
  - YOLOv8 (Ultralytics)
  - Imutils
  - Numpy

## Instalación

1. Clonar el repositorio o descargar el código fuente:
   ```
   https://github.com/spooky1703/Eco_VishonAI.git
   cd eco_vishionai
   ```

2. Instalar las dependencias:

   Si estás utilizando un entorno virtual (recomendado), actívalo antes de instalar las dependencias.

   ```
   pip install -r requirements.txt
   ```

   Si no tienes un archivo requirements.txt, instala las dependencias manualmente con el siguiente comando:

   ```
   pip install opencv-python-headless pillow ultralytics numpy imutils
   ```

3. Descargar y colocar el modelo YOLO:
   - **IMPORTANTE**: Debido a limitaciones de GitHub, el modelo YOLO no está incluido en el repositorio.
   - Descarga el modelo desde este link: [https://www.mediafire.com/folder/y6u6feknwpqh4/Modelos](https://www.mediafire.com/folder/y6u6feknwpqh4/Modelos)
   - Coloca el archivo descargado (`best.pt`) en la carpeta `Modelos/` del proyecto.

4. Colocar los recursos visuales:
   - Coloca las imágenes de contenedores de reciclaje en la carpeta `setop`:
     - Metal.png
     - vidrio.png
     - plastico.png
     - carton.png
     - medical.png
   - Coloca las imágenes de texto informativo en la misma carpeta `setUp`:
     - metaltxt.png
     - vidriotxt.png
     - plasticotxt.png
     - cartontxt.png
     - medicaltxt.png

## Estructura del Proyecto

```
eco_vishionai/
├── Modelos/
│   └── best.pt              # Modelo YOLOv8 preentrenado para la detección (descargar separadamente)
├── setop/
│   ├── Canva.png            # Imagen de fondo para la interfaz
│   ├── Metal.png            # Imagen del contenedor de metal
│   ├── vidrio.png           # Imagen del contenedor de vidrio
│   ├── plastico.png         # Imagen del contenedor de plástico
│   ├── carton.png           # Imagen del contenedor de cartón
│   ├── medical.png          # Imagen del contenedor médico
│   ├── metaltxt.png         # Texto explicativo para metal
│   ├── vidriotxt.png        # Texto explicativo para vidrio
│   ├── plasticotxt.png      # Texto explicativo para plástico
│   ├── cartontxt.png        # Texto explicativo para cartón
│   └── medicaltxt.png       # Texto explicativo para desechos médicos
└── main.py                  # Archivo principal de la aplicación
```

[El resto del README continúa sin cambios...]
## Uso del Programa

### 1. Iniciar la aplicación

Ejecuta el archivo principal `main.py` para iniciar la interfaz gráfica y la clasificación de imágenes en tiempo real:

```
python main.py
```

### 2. Interfaz de usuario

- La aplicación mostrará una ventana con una interfaz gráfica donde:
  - Video en vivo: Captura la imagen en tiempo real desde la cámara.
  - Detección en tiempo real: Cuando un objeto de basura es detectado, se dibuja un recuadro sobre el objeto con la clase de basura identificada.
  - Imágenes de referencia: Dependiendo del tipo de basura detectado, se mostrará una imagen del contenedor de reciclaje correspondiente.
  - Texto explicativo: También se muestra un texto explicativo del tipo de basura que se ha identificado.

### 3. Tipos de basura detectados

El modelo YOLO utilizado ha sido entrenado para detectar los siguientes tipos de basura:

- Metal
- Vidrio
- Plástico
- Cartón
- Desechos médicos

### 4. Escaneo y clasificación

El escaneo de la imagen se realiza automáticamente, con actualizaciones cada 10 ms. El usuario no necesita realizar ninguna acción adicional para que la detección ocurra.

## Estructura del Código

### 1. Módulos y librerías

- Tkinter: Para la interfaz gráfica.
- OpenCV: Para la captura de video y procesamiento de imágenes.
- YOLO: Modelo de detección de objetos preentrenado.
- PIL: Para la manipulación de imágenes.
- Imutils: Para redimensionar las imágenes.

### 2. Descripción de funciones principales

- `ventana_principal()`: Esta función crea la ventana de la aplicación y configura la cámara para la captura de video en tiempo real. También carga las imágenes de contenedores y textos.
- `Scanning()`: Función que ejecuta el modelo YOLO sobre la imagen de la cámara, analiza los objetos detectados y actualiza la interfaz con la información correspondiente (imágenes y textos).
- `images(img, imgtxt)`: Muestra las imágenes de contenedores y el texto explicativo correspondiente a la clase de basura detectada.

### 3. Modelo de Detección (YOLO)

El modelo YOLOv8 preentrenado (ubicado en `Modelos/best.pt`) se utiliza para detectar los tipos de basura. Cuando un objeto es detectado, el modelo devuelve las coordenadas de una caja delimitadora, la clase de objeto detectado y el nivel de confianza.

## Notas adicionales

### 1. Optimización del rendimiento

Si experimentas lentitud en la captura de video, asegúrate de que tu computadora esté ejecutando el proyecto de manera eficiente. En algunos casos, puede ser útil reducir la resolución de la cámara o utilizar un modelo YOLO más ligero.

### 2. Ampliación del modelo

Si deseas entrenar el modelo YOLO para detectar más tipos de basura o mejorar la precisión del modelo actual, puedes hacerlo proporcionando un conjunto de datos adecuado y volviendo a entrenar el modelo YOLO.
### 3. Uso del programa

Una vez que haya completado correctamente todos los pasos de instalación, debería poder ejecutar Eco_VishionAI en su computadora. Tenga en cuenta los siguientes puntos para un funcionamiento óptimo:

1. Permisos de cámara:
   Al ejecutar el programa por primera vez, se le solicitarán permisos de acceso a la cámara. Es posible que el script se cierre después de esta solicitud.

2. Reinicio del programa:
   Si el programa se cierra después de solicitar los permisos, simplemente reinícielo y ejecútelo nuevamente.

3. Preparación del entorno:
   - Apunte la cámara de su computadora hacia un área con un fondo despejado.
   - Asegúrese de que no haya objetos que puedan interrumpir el escaneo en el fondo.

4. Análisis de objetos:
   - Coloque los objetos que desea analizar en el área despejada frente a la cámara.
   - El programa detectará automáticamente los objetos y señalará qué tipo de residuo es cada uno.

5. Interpretación de resultados:
   Observe la pantalla para ver la clasificación de los residuos detectados. El programa indicará si el objeto es metal, vidrio, plástico, cartón o un desecho médico.

Recuerde que para obtener los mejores resultados, asegúrese de que los objetos estén claramente visibles y bien iluminados en el campo de visión de la cámara.


## Conclusión

ECO_VISHIONAI proporciona una solución visual intuitiva para la clasificación de basura, utilizando un modelo de detección robusto y una interfaz gráfica interactiva. Con una instalación adecuada y el uso de los recursos proporcionados, la aplicación es capaz de detectar y clasificar objetos en tiempo real, brindando una experiencia educativa y funcional para sus usuarios.
