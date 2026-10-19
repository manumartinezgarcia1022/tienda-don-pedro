from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

for linea in lineas[2:]:
    print("-", linea)
    partes = linea.split("$")
    precio = int(partes[1].replace(".", "").replace(",", ""))
    total_productos = total_productos + 1
    valor_inventario = valor_inventario + precio

print("Total de productos:", total_productos)
print("Valor del inventario: $" + str(valor_inventario))
