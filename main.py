import requests

def dish_fetch(num):
    
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

def show_available_dishes():
  
    url = "https://api-colombia.com/api/v1/TypicalDish"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            dishes = response.json()
            print("\n========================================")
            print("      PLATILLOS TIPICOS DISPONIBLES     ")
            print("========================================")
            for dish in dishes:
                dish_id = dish.get("id")
                dish_name = dish.get("name")
                print(f"  [ID: {dish_id}] -> {dish_name}")
            print("========================================\n")
        else:
            print("No se pudo obtener la lista de platillos.")
    except Exception:
        print("Error de conexión al obtener la lista de platillos.")

def main():
    print("Bienvenido al sistema de consulta de comida tipica")
    
    
    show_available_dishes()

    mientras_activo = True
    while mientras_activo:
        print("--- MENU DE OPCIONES ---")
        print("1. Consultar platillo por ID")
        print("2. Ver lista de platillos de nuevo")
        print("3. Salir")

        opcion = input("Seleccione una opcion (1, 2 o 3): ").strip()

        if opcion == "1":
            num = input("Ingrese el ID del platillo que desea ver: ").strip()
            if num.isdigit():
                data = dish_fetch(int(num))
                if data and "name" in data:
                    print("\n----------------------------------------")
                    print(f"Nombre: {data.get('name', 'N/A')}")
                    print(f"ID: {data.get('id', 'N/A')}")
                    print(f"Descripcion: {data.get('description', 'Sin descripcion disponible')}")
                    print("----------------------------------------\n")
                else:
                    print("\nNo se encontro informacion para ese ID.\n")
            else:
                print("\nPor favor, ingrese un numero entero valido.\n")

        elif opcion == "2":
            show_available_dishes()

        elif opcion == "3":
            print("Saliendo del programa...")
            mientras_activo = False
        else:
            print("\nOpcion no valida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()