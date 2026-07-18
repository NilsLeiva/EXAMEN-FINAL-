prendas = {
    'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
    'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
    'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
    'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
    'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
    'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],
}

bodega = {
    'S001': [7990, 12],
    'S002': [19990, 0],
    'S003': [29990, 3],
    'S004': [24990, 6],
    'S005': [17990, 8],
    'S006': [14990, 2],
}


def validar_codigo(codigo):
    return codigo.strip() != "" and codigo.strip().upper() not in prendas


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_categoria(categoria):
    return categoria.strip() != ""


def validar_talla(talla):
    return talla.strip() != ""


def validar_color(color):
    return color.strip() != ""


def validar_material(material):
    return material.strip() != ""


def validar_es_unisex(valor):
    return valor.lower() in ("s", "n")


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0


def unidades_categoria(categoria):
    total = 0
    for codigo, datos in prendas.items():
        if datos[1].lower() == categoria.lower():
            total += bodega[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo, datos in bodega.items():
        precio, unidades = datos
        if p_min <= precio <= p_max and unidades != 0:
            nombre = prendas[codigo][0]
            resultados.append(f"{nombre}--{codigo}")
    resultados.sort()
    if resultados:
        print(f"Las prendas encontradas son: {resultados}")
    else:
        print("No hay prendas en ese rango de precios.")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.strip().upper()
    if codigo not in bodega:
        return False
    bodega[codigo][0] = nuevo_precio
    return True


def eliminar_prenda(codigo):
    codigo = codigo.strip().upper()
    if codigo not in prendas:
        return False
    del prendas[codigo]
    del bodega[codigo]
    return True


def agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
    codigo = codigo.strip().upper()
    if codigo in prendas:
        return False
    prendas[codigo] = [nombre, categoria, talla, color, material, es_unisex]
    bodega[codigo] = [precio, unidades]
    return True


def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Unidades por categoría")
        print("2. Búsqueda de prendas por rango de precio")
        print("3. Actualizar precio de prenda")
        print("4. Agregar prenda")
        print("5. Eliminar prenda")
        print("6. Salir")
        print("=====================================")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            categoria = input("Ingrese categoría a consultar: ")
            unidades_categoria(categoria)

        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")

            if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                busqueda_precio(p_min, p_max)
            else:
                print("Debe ingresar valores enteros")

        elif opcion == "3":
            repetir = "s"
            while repetir == "s":
                codigo = input("Ingrese código de la prenda: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                except ValueError:
                    print("Debe ingresar un valor entero")
                    repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()
                    continue

                if actualizar_precio(codigo, nuevo_precio):
                    print("Precio actualizado")
                else:
                    print("El código no existe")

                repetir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

        elif opcion == "4":
            codigo = input("Ingrese código de la prenda: ")
            if not validar_codigo(codigo):
                print("El código no es válido o ya existe")
                continue

            nombre = input("Ingrese nombre: ")
            if not validar_nombre(nombre):
                print("El nombre no es válido")
                continue

            categoria = input("Ingrese categoría: ")
            if not validar_categoria(categoria):
                print("La categoría no es válida")
                continue

            talla = input("Ingrese talla: ")
            if not validar_talla(talla):
                print("La talla no es válida")
                continue

            color = input("Ingrese color: ")
            if not validar_color(color):
                print("El color no es válido")
                continue

            material = input("Ingrese material: ")
            if not validar_material(material):
                print("El material no es válido")
                continue

            unisex_ingresado = input("¿Es unisex? (s/n): ")
            if not validar_es_unisex(unisex_ingresado):
                print("Debe ingresar 's' o 'n'")
                continue
            es_unisex = unisex_ingresado.lower() == "s"

            try:
                precio = int(input("Ingrese precio: "))
            except ValueError:
                print("El precio debe ser un número entero")
                continue
            if not validar_precio(precio):
                print("El precio no es válido")
                continue

            try:
                unidades = int(input("Ingrese unidades: "))
            except ValueError:
                print("Las unidades deben ser un número entero")
                continue
            if not validar_unidades(unidades):
                print("Las unidades no son válidas")
                continue

            if agregar_prenda(codigo, nombre, categoria, talla, color, material, es_unisex, precio, unidades):
                print("Prenda agregada")
            else:
                print("El código ya existe")

        elif opcion == "5":
            codigo = input("Ingrese código de la prenda: ")
            if eliminar_prenda(codigo):
                print("Prenda eliminada")
            else:
                print("El código no existe")

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida")


main()