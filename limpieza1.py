import csv

input_file = 'pokemon.csv'
output_file = 'resultado_filtrado.csv'

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
        
        new_row = {'name': name, 'weight_kg': weight_kg, 'base_total': base_total, 'capture_rate': capture_rate}
        writer.writerow(new_row)
