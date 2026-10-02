import requests

def dish_fetch(num):
    # La prueba de pytest solo evalúa esta función aislada
    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}

def main():
    print("Bienvenido al sistema de consulta de comida tipica")
    
    mientras_activo = True
    while mientras_activo:
        print("\n--- menu de platillos colombianos ---")
        print("1. Consultar platillo por ID")
        print("2. Salir")
        
        opcion = input("Seleccione una opcion (1 o 2): ").strip()
        
        if opcion == "1":
            numero_id = input("Ingrese el ID del platillo: ").strip()
            
            if numero_id.isdigit():
                datos = dish_fetch(int(numero_id))
                
                nombre = datos.get("name")
                descripcion = datos.get("description")
                
                if nombre:
                    print("\n" + "="*40)
                    print("Nombre del platillo:", nombre)
                    print("Descripcion:", descripcion)
                    print("="*40)
                else:
                    print("No se encontro un platillo con ese ID.")
            else:
                print("Por favor ingrese solo numeros enteros.")
                
        elif opcion == "2":
            print("Gracias por usar el sistema. Hasta luego.")
            mientras_activo = False
        else:
            print("Opcion no valida. Intente de nuevo.")

if __name__ == "__main__":
    main()