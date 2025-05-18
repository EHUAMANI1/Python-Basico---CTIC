# Validacion de Tipo de Crédito

import pandas as pd
import os

# Ruta al archivo de origen
base_dir = os.getcwd()

# Definir las rutas a ambos archivos
archivo_consolidado = os.path.join(base_dir, "Data", "Entrada", "04 CONSOLIDADOCOMPLETOC 30-04-2025.xlsm")
archivo_minutas = os.path.join(base_dir, "Data", "Entrada", "Minutas.xlsx")

# Leer la hoja "CONSOLIDADO SIMPLE" del primer archivo Excel
df_consolidado = pd.read_excel(archivo_consolidado, sheet_name="CONSOLIDADO SIMPLE")

# Filtrar la columna "STATUS" para quedarnos solo con las filas que contienen "Firmo"
df_consolidado_filtrado = df_consolidado[df_consolidado["STATUS"] == "Firmo"]

# Leer la hoja "Consolidado" del segundo archivo Excel (Minutas)
df_minutas = pd.read_excel(archivo_minutas, sheet_name="Consolidado")

# Limpiar los nombres de las columnas en ambos DataFrames
df_consolidado_filtrado.columns = df_consolidado_filtrado.columns.str.strip()
df_minutas.columns = df_minutas.columns.str.strip()

# Convertir las columnas 'CODIGO' y 'codigo' a mayúsculas
df_consolidado_filtrado['CODIGO'] = df_consolidado_filtrado['CODIGO'].apply(lambda x: str(x).upper() if isinstance(x, str) else x)
df_minutas['codigo'] = df_minutas['codigo'].apply(lambda x: str(x).upper() if isinstance(x, str) else x)

# Verificar las columnas de ambos DataFrames
print("Columnas en df_consolidado_filtrado:")
print(df_consolidado_filtrado.columns)

print("\nColumnas en df_minutas:")
print(df_minutas.columns)

# Realizar el merge (intersección) en las columnas 'CODIGO' de df_consolidado y 'codigo' de df_minutas
df_intersectado = pd.merge(df_consolidado_filtrado, df_minutas, left_on="CODIGO", right_on="codigo", how="inner")

# Verificar las columnas después del merge
print("\nColumnas en df_intersectado:")
print(df_intersectado.columns)

# Seleccionar las columnas deseadas para el DataFrame final
columnas_deseadas = [
    "codigo", "codigo_proforma", "nombre_proyecto", "tipo_unidad", "estado_comercial", 
    "etiqueta", "fecha_pago", "nombres_cliente", "apellidos_cliente", "fecha_inicio", 
    "fecha_fin", "STATUS", "FECHA DE STATUS"
]

# Crear el DataFrame final con las columnas seleccionadas
df_final = df_intersectado[columnas_deseadas]

# Mostrar las primeras filas del DataFrame final para verificar
print(df_final.head())

# Exportar el DataFrame final a un archivo Excel
archivo_salida = os.path.join(base_dir, "Data", "Salida", "FRAME_RESULTADO.xlsx")
df_final.to_excel(archivo_salida, index=False)

print(f"✅ Archivo exportado correctamente en:\n{archivo_salida}")
