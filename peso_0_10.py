import csv

input_file = 'resultado_sin_ceros_o_vacios.csv'
output_file = 'resultado_normalizado.csv'

# Función para normalizar weight_kg en el rango [0, 10]
def normalizar_weight_kg(weight_kg, min_weight_kg, max_weight_kg):
    return 10 * (float(weight_kg) - min_weight_kg) / (max_weight_kg - min_weight_kg)

# Calcular los valores mínimo y máximo de weight_kg
min_weight_kg = float('inf')
max_weight_kg = float('-inf')

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        weight_kg = float(row['weight_kg'])
        min_weight_kg = min(min_weight_kg, weight_kg)
        max_weight_kg = max(max_weight_kg, weight_kg)

# Leer el archivo CSV y procesar las filas
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ['name', 'weight_kg', 'base_total', 'capture_rate']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        name = row['name']
        weight_kg = row['weight_kg']
        base_total = row['base_total']
        capture_rate = row['capture_rate']

        weight_kg_normalizado = normalizar_weight_kg(weight_kg, min_weight_kg, max_weight_kg)

        new_row = {'name': name, 'weight_kg': weight_kg_normalizado, 'base_total': base_total, 'capture_rate': capture_rate}
        writer.writerow(new_row)
