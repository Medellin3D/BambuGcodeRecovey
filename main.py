def modificar_gcode(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file:
        lines = file.readlines()
    
    with open(archivo_salida, 'w') as file:
        for index, line in enumerate(lines):
            if index >= 663:  # Las líneas empiezan desde 0, así que la línea 664 es el índice 663
                parts = line.split()
                new_line = []
                for part in parts:
                    if part.startswith('Z'):
                        try:
                            z_val = float(part[1:])
                            z_val -= 201.2
                            new_line.append(f'Z{z_val:.4f}')
                        except ValueError:
                            new_line.append(part)  # Si no es un número, se deja igual
                    else:
                        new_line.append(part)
                file.write(' '.join(new_line) + '\n')
            else:
                file.write(line)

    # Verificación de valores Z negativos
    with open(archivo_salida, 'r') as file:
        for line in file:
            if 'Z' in line:
                parts = line.split()
                for part in parts:
                    if part.startswith('Z'):
                        try:
                            z_val = float(part[1:])
                            if z_val < 0:
                                raise ValueError(f"Valor Z negativo encontrado: Z{z_val:.4f}")
                        except ValueError:
                            continue  # Ignorar si no es un número

# Nombres de los archivos de entrada y salida
archivo_entrada = 'plate.gcode'
archivo_salida = 'archivo_modificado.gcode'

# Ejecuta la función para modificar el archivo G-code y verificar valores negativos de Z
try:
    modificar_gcode(archivo_entrada, archivo_salida)
    print("Modificaciones completadas sin valores Z negativos.")
except ValueError as e:
    print(e)
