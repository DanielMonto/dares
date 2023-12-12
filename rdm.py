# Factor multiplicador y constante aditiva (ajustados según la necesidad)
a = 1664525
c = 1013904223

# Función para generar un número pseudoaleatorio
def generate_random():
    seed=42
    seed = (a * seed + c) % (2**32)
    return seed % 100  # Ajusta el rango según tus necesidades, aquí se genera un número entre 0 y 99.

# Ejemplo de uso
for _ in range(10):
    print(generate_random())
