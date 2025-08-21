import re

def validar_username(username: str) -> bool:
    """
    Valida un nombre de usuario.
    Reglas:
    - Entre 3 y 16 caracteres
    - Solo letras, números y guiones bajos (_)
    """
    patron = r'^[A-Za-z0-9_]{3,16}$'
    return bool(re.match(patron, username))

def main():
    print("=== Validador de Usernames ===")
    print("Reglas: 3-16 caracteres, solo letras, números y _")
    print("Escribe 'salir' para terminar.\n")

    while True:
        usuario = input("Ingrese un username: ")
        
        if usuario.lower() == "salir":
            print("Programa finalizado. 👋")
            break

        if validar_username(usuario):
            print("✅ Username válido\n")
        else:
            print("❌ Username inválido\n")

if __name__ == "__main__":
    main()