import csv

input_file = 'resultado_puntos.csv'

# Leer el archivo CSV y almacenar las filas en una lista
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    pokemon_list = [row for row in reader]

# Ordenar la lista de Pokémon por la columna 'puntos' en orden descendente
sorted_pokemon_list = sorted(pokemon_list, key=lambda x: float(x['puntos']), reverse=True)

# Seleccionar los 6 Pokémon con más puntos
top_6_pokemon = sorted_pokemon_list[:6]

# Imprimir los 6 Pokémon con más puntos
for pokemon in top_6_pokemon:
    print(pokemon)
#Este código imprimirá en la consola los 6 Pokémon con más puntos. Si deseas guardar estos 6 Pokémon en un nuevo archivo CSV, puedes agregar el siguiente código después de la última línea:
output_file = 'top_6_pokemon.csv'

with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ['name', 'weight_kg', 'base_total', 'capture_rate', 'puntos']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for pokemon in top_6_pokemon:
        writer.writerow(pokemon)
