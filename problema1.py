# ---------- FUNCIONES AUXILIARES ----------

def tiene_longitud_valida(contrasena):
    return len(contrasena) >= 8 and len(contrasena) <= 20


def tiene_mayuscula(contrasena):
    for c in contrasena:
        if c.isupper():
            return True
    return False


def tiene_minuscula(contrasena):
    for c in contrasena:
        if c.islower():
            return True
    return False


def tiene_numero(contrasena):
    for c in contrasena:
        if c.isdigit():
            return True
    return False


def tiene_especial(contrasena):
    especiales = "!@#$%^&*"
    for c in contrasena:
        if c in especiales:
            return True
    return False


# ---------- FUNCIÓN PRINCIPAL ----------

def validar_contrasena(contrasena):
    return (
        tiene_longitud_valida(contrasena) and
        tiene_mayuscula(contrasena) and
        tiene_minuscula(contrasena) and
        tiene_numero(contrasena) and
        tiene_especial(contrasena)
    )


# ---------- PROGRAMA ----------

while True:
    contrasena = input("Ingrese una contraseña: ")

    if validar_contrasena(contrasena):
        print("✅ Contraseña válida")
        break
    else:
        print("❌ La contraseña no cumple con:")

        if not tiene_longitud_valida(contrasena):
            print("- Debe tener entre 8 y 20 caracteres")

        if not tiene_mayuscula(contrasena):
            print("- Debe tener al menos una mayúscula")

        if not tiene_minuscula(contrasena):
            print("- Debe tener al menos una minúscula")

        if not tiene_numero(contrasena):
            print("- Debe tener al menos un número")

        if not tiene_especial(contrasena):
            print("- Debe tener un carácter especial !@#$%^&*")

        print()