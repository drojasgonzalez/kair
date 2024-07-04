import csv  

def save_to_csv(data, filename='books.csv'):

    keys = data[0].keys()  # Obtiene los nombres de columnas del primer diccionario en la lista

    # Abre el archivo CSV en modo escritura (write) 
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        # Crea un escritor de diccionarios para escribir datos en el archivo CSV
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()  # Escribe la cabecera (nombres de columnas)
        # Escribe todas las filas en el archivo CSV
        dict_writer.writerows(data)
