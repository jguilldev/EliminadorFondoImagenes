import os
from rembg import remove
from PIL import Image
from tqdm import tqdm  # Para mostrar una barra de progreso

# Definir las rutas de las carpetas
input_folder = "imagenes_entrada"  # Carpeta con imágenes originales
output_folder = "imagenes_salida"  # Carpeta para guardar imágenes sin fondo

# Crear las carpetas si no existen
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Obtener la lista de archivos a procesar
image_files = [
    file_name for file_name in os.listdir(input_folder)
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg'))
]

# Si no hay imágenes, mostrar un mensaje y salir
if not image_files:
    print(f"No se encontraron imágenes en la carpeta '{input_folder}'.")
    print("Por favor, sube imágenes y vuelve a ejecutar el script.")
else:
    print(f"Se encontraron {len(image_files)} imágenes en '{input_folder}'.")
    print("Procesando imágenes...")

    # Procesar cada imagen con una barra de progreso
    for file_name in tqdm(image_files, desc="Progreso", unit="imagen"):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            # Abrir y procesar la imagen
            with open(input_path, 'rb') as input_file:
                img_data = remove(input_file.read())
                # Guardar la imagen procesada
                with open(output_path, 'wb') as output_file:
                    output_file.write(img_data)
        except Exception as e:
            print(f"\n[Error] No se pudo procesar '{file_name}': {e}")

    print(f"\n¡Procesamiento completado! Las imágenes sin fondo están en '{output_folder}'.")
