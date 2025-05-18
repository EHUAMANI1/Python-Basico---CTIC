# Imagen

from PIL import Image, ImageDraw
import math

# Crear una imagen con fondo blanco
img = Image.new('RGB', (500, 500), color='white')
draw = ImageDraw.Draw(img)

# Definir colores
colores = ['#FF5733', '#33FF57', '#3357FF', '#F0FF33']

# Dibujar líneas onduladas
for i in range(0, 500, 20):
    for j, color in enumerate(colores):
        # Crear ondas con seno (sinusoidal) para generar la forma
        for x in range(0, 500):
            y = int(250 + 100 * math.sin((x + i) * 0.05 + j))  # Fórmula para la onda
            draw.point((x, y), fill=color)

# Guardar y mostrar la imagen
img.save('patron_ondas_abstracto.png')
img.show()
