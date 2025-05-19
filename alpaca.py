import os
import json

ARCHIVO = 'curso/alpacas.json'
EDADES_VALIDAS = {'DL', '2D', '4D', 'BLL'}
EDADES_DESCRIPCION = {
    'DL': 'Diente de Leche',
    '2D': 'Dos Dientes',
    '4D': 'Cuatro Dientes',
    'BLL': 'Boca Llena'
}

def leer_alpacas():
    if not os.path.exists(ARCHIVO):
        return []
    try:
        with open(ARCHIVO, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠️ Error al leer el archivo: {e}")
        return []

def guardar_alpacas(alpacas):
    try:
        with open(ARCHIVO, 'w') as file:
            json.dump(alpacas, file, indent=2)
    except IOError as e:
        print(f"⚠️ Error al guardar el archivo: {e}")

def mostrar_alpacas(alpacas):
    if not alpacas:
        print("No hay alpacas registradas.")
    else:
        print("\nLista de Alpacas:")
        for i, a in enumerate(alpacas, 1):
            edad_cod = a['edad']
            edad_desc = EDADES_DESCRIPCION.get(edad_cod, 'Desconocida')
            print(f"{i}. Arete: {a['arete']} - Edad: {edad_cod} ({edad_desc}) - Sexo: {a['sexo']} - Peso: {a['peso']:.2f} kg")

def ingresar_alpaca(alpacas):
    arete = input("Código de arete: ")
    if any(a['arete'] == arete for a in alpacas):
        print("❌ Ya existe una alpaca con ese código de arete.")
        return
    edad = input("Edad (DL/2D/4D/BLL): ").upper()
    if edad not in EDADES_VALIDAS:
        print("❌ Edad inválida. Usa DL, 2D, 4D o BLL.")
        return
    sexo = input("Sexo (Macho/Hembra): ")
    try:
        peso = float(input("Peso: "))
    except ValueError:
        print("❌ Peso inválido.")
        return
    alpacas.append({'arete': arete, 'edad': edad, 'sexo': sexo, 'peso': peso})
    guardar_alpacas(alpacas)
    print("✅ Alpaca ingresada con éxito.")

def editar_alpaca(alpacas):
    mostrar_alpacas(alpacas)
    try:
        idx = int(input("Número de la alpaca a editar: ")) - 1
    except ValueError:
        print("❌ Índice inválido.")
        return

    if 0 <= idx < len(alpacas):
        alpaca = alpacas[idx]
        print("Deja en blanco para mantener el valor actual.")
        nuevo_arete = input(f"Código de arete ({alpaca['arete']}): ") or alpaca['arete']
        nueva_edad = input(f"Edad ({alpaca['edad']}) [DL/2D/4D/BLL]: ").upper() or alpaca['edad']
        if nueva_edad not in EDADES_VALIDAS:
            print("❌ Edad inválida. Cambios no guardados.")
            return
        nuevo_sexo = input(f"Sexo ({alpaca['sexo']}): ") or alpaca['sexo']
        nuevo_peso = input(f"Peso ({alpaca['peso']}): ") or alpaca['peso']
        try:
            alpacas[idx] = {
                'arete': nuevo_arete,
                'edad': nueva_edad,
                'sexo': nuevo_sexo,
                'peso': float(nuevo_peso)
            }
            guardar_alpacas(alpacas)
            print("✏️ Alpaca actualizada.")
        except ValueError:
            print("❌ Datos inválidos. Cambios no guardados.")
    else:
        print("❌ Índice fuera de rango.")

def eliminar_alpaca(alpacas):
    mostrar_alpacas(alpacas)
    try:
        idx = int(input("Número de la alpaca a eliminar: ")) - 1
    except ValueError:
        print("❌ Índice inválido.")
        return

    if 0 <= idx < len(alpacas):
        eliminada = alpacas[idx]
        confirm = input(f"¿Estás seguro de eliminar el arete '{eliminada['arete']}'? (s/n): ")
        if confirm.lower() == 's':
            alpacas.pop(idx)
            guardar_alpacas(alpacas)
            print(f"🗑️ Alpaca con arete '{eliminada['arete']}' eliminada.")
        else:
            print("❌ Eliminación cancelada.")
    else:
        print("❌ Índice fuera de rango.")

def menu():
    alpacas = leer_alpacas()
    while True:
        print("\n--- Menú Alpacas ---")
        print("1. Ver alpacas")
        print("2. Ingresar nueva alpaca")
        print("3. Editar alpaca")
        print("4. Eliminar alpaca")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            mostrar_alpacas(alpacas)
        elif opcion == '2':
            ingresar_alpaca(alpacas)
        elif opcion == '3':
            editar_alpaca(alpacas)
        elif opcion == '4':
            eliminar_alpaca(alpacas)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == '__main__':
    menu()