#1
ventas = [{
    "fecha": "2024-01-03",
    "producto": "naranja",
    "cantidad": 7,
    "precio": 1000
},
{
    "fecha": "2024-01-04",
    "producto": "naranja",
    "cantidad": 8,
    "precio": 1000
},
{
    "fecha": "2024-01-04",
    "producto": "naranja",
    "cantidad": 2,
    "precio": 1000
},
{
    "fecha": "2024-01-04",
    "producto": "manzana",
    "cantidad": 7,
    "precio": 900
},
{
    "fecha": "2024-01-03",
    "producto": "manzana",
    "cantidad": 6,
    "precio": 900
},
{
    "fecha": "2024-01-03",
    "producto": "manzana",
    "cantidad": 8,
    "precio": 900
},
{
    "fecha": "2024-01-03",
    "producto": "manzana",
    "cantidad": 10,
    "precio": 900
},
{
    "fecha": "2024-01-04",
    "producto": "naranja",
    "cantidad": 7,
    "precio": 1000
},
{
    "fecha": "2024-01-04",
    "producto": "manzana",
    "cantidad": 7,
    "precio": 900
},
{
    "fecha": "2024-01-04",
    "producto": "manzana",
    "cantidad": 6,
    "precio": 900
}]

#2

ingresos = 0
for venta in ventas:
    ingresos += (venta["cantidad"]*venta["precio"])
print(f"El total de ingresos es: ${ingresos}")


#3

from collections import defaultdict

ventas_por_producto = defaultdict(int)
for venta in ventas:
    ventas_por_producto[venta["producto"]] += venta["cantidad"]

producto_mas_vendido = max(ventas_por_producto.items(), key=lambda x: x[1])
print(ventas_por_producto)
print(f"Producto más vendido: {producto_mas_vendido[0]} ({producto_mas_vendido[1]} unidades)")


#4 Promedio de Precio por Producto
precios_por_producto = defaultdict(lambda: [0.0, 0])  # [suma precios, total unidades]
for venta in ventas:
    precios_por_producto[venta["producto"]][0] += venta["precio"] * venta["cantidad"]
    precios_por_producto[venta["producto"]][1] += venta["cantidad"]

promedios_por_producto = {
    producto: total / cantidad for producto, (total, cantidad) in precios_por_producto.items()
}
print(promedios_por_producto)

# 5. Ventas por Día
ingresos_por_dia = defaultdict(float)
for venta in ventas:
    ingresos_por_dia[venta["fecha"]] += venta["cantidad"] * venta["precio"]


# 6. Representación de Datos
resumen_ventas = {}
for producto in ventas_por_producto.keys():
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = promedios_por_producto[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": round(ingresos_totales_producto),
        "precio_promedio": round(precio_promedio)
    }

# Imprimir el resumen de ventas
print("\nResumen por producto:")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}: {resumen}")

# Imprimir ingresos por día
print("\nIngresos por día:")
for fecha, ingreso in sorted(ingresos_por_dia.items()):
    print(f"{fecha}: ${round(ingreso)}")