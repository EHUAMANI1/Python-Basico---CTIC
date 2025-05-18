from PIL import Image, ImageDraw, ImageFont

# Tamaño de la imagen
ancho, alto = 800, 600
color_fondo = (40, 120, 200)  # Azul

# Crear imagen
imagen = Image.new("RGB", (ancho, alto), color_fondo)
dibujo = ImageDraw.Draw(imagen)
fuente = ImageFont.load_default()

# Texto centrado
texto = "Fondo generado con Python"
bbox = dibujo.textbbox((0, 0), texto, font=fuente)
ancho_texto = bbox[2] - bbox[0]
alto_texto = bbox[3] - bbox[1]
pos_x = (ancho - ancho_texto) // 2
pos_y = (alto - alto_texto) // 2

# Dibujar texto centrado
dibujo.text((pos_x, pos_y), texto, fill="white", font=fuente)

# Guardar la imagen en el mismo directorio
nombre_imagen = "fondo_visual_python.png"
imagen.save(nombre_imagen)

print("✅ Imagen creada correctamente.")

imagen.save(nombre_imagen)

print("✅ Imagen creada correctamente.")
