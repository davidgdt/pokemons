import csv

input_file = 'resultado_normalizado.csv'
output_file = 'resultado_base_total_normalizado.csv'

# Función para normalizar base_total en el rango [0, 10]
def normalizar_base_total(base_total, min_base_total, max_base_total):
    return 10 * (float(base_total) - min_base_total) / (max_base_total - min_base_total)

# Calcular los valores mínimo y máximo de base_total
min_base_total = float('inf')
max_base_total = float('-inf')

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        base_total = float(row['base_total'])
        min_base_total = min(min_base_total, base_total)
        max_base_total = max(max_base_total, base_total)

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

        base_total_normalizado = normalizar_base_total(base_total, min_base_total, max_base_total)

        new_row = {'name': name, 'weight_kg': weight_kg, 'base_total': base_total_normalizado, 'capture_rate': capture_rate}
        writer.writerow(new_row)
