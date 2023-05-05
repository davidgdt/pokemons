import csv

input_file = 'resultado_base_total_normalizado.csv'
output_file = 'resultado_puntos.csv'

# Función para normalizar puntos en el rango [0, 1]
def normalizar_puntos(puntos, min_puntos, max_puntos):
    return (float(puntos) - min_puntos) / (max_puntos - min_puntos)

# Calcular los valores mínimo y máximo de puntos
min_puntos = float('inf')
max_puntos = float('-inf')

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        weight_kg = float(row['weight_kg'])
        base_total = float(row['base_total'])
        if weight_kg != 0:
            puntos = base_total / weight_kg
            min_puntos = min(min_puntos, puntos)
            max_puntos = max(max_puntos, puntos)

# Leer el archivo CSV y procesar las filas
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['name', 'weight_kg', 'base_total', 'capture_rate', 'puntos']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        name = row['name']
        weight_kg = float(row['weight_kg'])
        base_total = float(row['base_total'])
        capture_rate = row['capture_rate']

        if weight_kg != 0:
            puntos = base_total / weight_kg
            puntos_normalizados = normalizar_puntos(puntos, min_puntos, max_puntos)
        else:
            puntos_normalizados = 0

        new_row = {'name': name, 'weight_kg': weight_kg, 'base_total': base_total, 'capture_rate': capture_rate, 'puntos': puntos_normalizados}
        writer.writerow(new_row)

