import pandas as pd
import os

# Ruta al archivo de origen
base_dir = os.getcwd()

archivo_consolidado = os.path.join(base_dir, "Data", "Entrada", "04 CONSOLIDADOCOMPLETOC 30-04-2025 (1).xlsm")
print("Ruta del archivo:", archivo_consolidado)

# Ruta de salida
archivo_salida = os.path.join(base_dir, "Data", "Salida","COMITE_ABRIL_EXTRAIDO.xlsx")

# Verificar si el archivo de origen existe
if not os.path.exists(archivo_consolidado):
    print(f"Archivo no encontrado: {archivo_consolidado}")
else:
    try:
        # Leer el archivo Excel
        df_consolidado = pd.read_excel(archivo_consolidado, sheet_name='CONSOLIDADO COMPLETO')

        # Seleccionar las columnas necesarias (PROYECTO, CODIGO, INMUEBLE, STATUS, MEDIO, FECHA DE 1ER CONTACTO)
        columnas_extraer = ['CODIGO', 'PROYECTO', 'INMUEBLE', 'STATUS', 'MEDIO', 'FECHA DE 1ER CONTACTO']
        df_extract = df_consolidado[columnas_extraer].copy()

        # Filtrar los registros con STATUS "Firmo", "Pendiente Firma" y "Caida" y solo "Departamento" en INMUEBLE
        df_extract = df_extract[df_extract['STATUS'].isin(['Firmo', 'Pendiente Firma', 'Caida'])]
        df_extract = df_extract[df_extract['INMUEBLE'] == 'Departamento']

        # Mapeo para la columna 'MEDIO' según lo solicitado
        medio_map = {
            'Branding caseta': 'Paso / vive por la zona',
            'Otras': 'Otros',
            'Volanteo': 'Llamadas/Volantes',
            'A donde vivir': 'AdondeVivir',
            'Nexo': 'Nexo inmobilario',
            'Agente Brava': 'Corredor',
            'Agente Decateca': 'Corredor',
            'Agente @': 'Corredor',
            'Agente Capitalizarme': 'Corredor',
            'Agente Erika': 'Corredor',
            'Agente Fenix': 'Corredor',
            'Agente Properati': 'Corredor',
            'Agente Nexo': 'Corredor',
            'Agente Natalia': 'Corredor',
            'Agente ICRECER': 'Corredor',
            'Agente Remax': 'Corredor',
            'Call Center - Call branding': 'Paso / vive por la zona',
            'Call Center - Facebook': 'Facebook',
            'Call Center - Web': 'Web',
            'Call Center - A donde vivir': 'AdondeVivir',
            'Call Center - Urbania': 'Urbania',
            'Call Center - Nexo': 'Nexo inmobilario',
            'Call Center - Feria Nexo': 'Feria',
            'Call Center - Feria expo Urbania': 'Feria',
            'Call Center - Volanteo': 'Llamadas/Volantes',
            'Modulo Unicachi': 'Otros',
            'Demolition Fest': 'Otros',
            'Modulo Mega Plaza': 'Otros',
            'Feria Infocasas': 'Otros',
            'Evento Leuro': 'Otros',
            'Cliente Albamar': 'Recontacto',
            'Feria BCP': 'Otros'
        }

        # Aplicar el mapeo de 'MEDIO'
        df_extract['MEDIO'] = df_extract['MEDIO'].map(medio_map).fillna(df_extract['MEDIO'])

        # Verificar si la carpeta de salida existe, si no, crearla
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        # Exportar los datos a un archivo Excel
        df_extract.to_excel(archivo_salida, index=False)

        print(f"Archivo exportado exitosamente a: {archivo_salida}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
