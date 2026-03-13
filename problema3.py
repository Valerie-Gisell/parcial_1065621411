# -------- FUNCIONES --------

def total_caracteres(texto):
    return len(texto)

def total_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def total_oraciones(texto):
    contador = 0
    for c in texto:
        if c in ".!?":
            contador += 1
    return contador

def palabra_mas_larga(texto):
    palabras = texto.split()
    mas_larga = palabras[0]

    for p in palabras:
        if len(p) > len(mas_larga):
            mas_larga = p

    return mas_larga

def palabra_mas_corta(texto):
    palabras = texto.split()
    mas_corta = palabras[0]

    for p in palabras:
        if len(p) < len(mas_corta):
            mas_corta = p

    return mas_corta

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = 0

    for c in texto:
        if c in vocales:
            contador += 1

    return contador

def contar_consonantes(texto):
    vocales = "aeiouAEIOU"
    contador = 0

    for c in texto:
        if c.isalpha() and c not in vocales:
            contador += 1

    return contador


# -------- PROGRAMA PRINCIPAL --------

texto = input("Ingrese un texto: ").strip()

if texto == "":
    print("Error: el texto no puede estar vacío.")
else:
    print("\n--- ESTADÍSTICAS DEL TEXTO ---")
    print("Total de caracteres:", total_caracteres(texto))
    print("Total de palabras:", total_palabras(texto))
    print("Total de oraciones:", total_oraciones(texto))
    print("Palabra más larga:", palabra_mas_larga(texto))
    print("Palabra más corta:", palabra_mas_corta(texto))
    print("Número de vocales:", contar_vocales(texto))
    print("Número de consonantes:", contar_consonantes(texto))