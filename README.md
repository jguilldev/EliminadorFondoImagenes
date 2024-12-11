# Eliminador de Fondo de Imágenes

Un sencillo script de Python que permite eliminar el fondo de múltiples imágenes automáticamente. Este proyecto utiliza la biblioteca [`rembg`](https://github.com/danielgatis/rembg) para procesar las imágenes y guardarlas con fondo transparente en una carpeta específica.

## Características
- Procesa múltiples imágenes de manera automática.
- Elimina el fondo y guarda las imágenes con fondo transparente.
- Fácil de usar, solo necesitas subir tus imágenes a la carpeta designada.
- Incluye manejo de errores y barra de progreso para una mejor experiencia de usuario.

## Requisitos
Antes de empezar, asegúrate de tener instalado:
- Python 3.8 o superior.

## Instalación y Configuración
Sigue estos pasos para configurar y ejecutar el proyecto:

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/EliminadorFondoImagenes.git
   cd EliminadorFondoImagenes

 2. Asegúrate de que el proyecto tenga la siguiente estructura:

EliminadorFondoImagenes/
├── index.py              # Script principal
├── imagenes_entrada/     # Carpeta donde colocar las imágenes originales
├── imagenes_salida/      # Carpeta donde se guardan las imágenes procesadas
├── README.md             # Este archivo

3. Abre la terminal:

Si estás usando un entorno de desarrollo como VS Code, presiona Ctrl + Ñ para abrir la terminal.
Instala las dependencias necesarias: Ejecuta el siguiente comando para instalar las bibliotecas requeridas:

pip install rembg Pillow tqdm

pip install rembg Pillow tqdm

pip install rembg Pillow tqdm

4. Ejecuta el script(desde la terminal): Para procesar las imágenes y eliminar sus fondos, ejecuta:

python index.py

5. Espera que el programa se ejecute y obtendras tus imagenes en la carpeta imagenes de salida. 




