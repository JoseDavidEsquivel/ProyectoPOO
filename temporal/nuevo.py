class Productos():

    def listarProductos(self) -> bool:
        return False

    def insertarProducto(self, sku:str, nombre:str, unidad:str) -> bool:
        print(f"INSERTAR: SKU: {sku} ,Nombre: {nombre} , Unidad: {unidad}")
        return True
    def actualizarProducto(self) -> bool:
        sku= input("SKU: ")
        nombre = input("Nombre: ")
        unidad = input("Unidad: ")
        print(f"ACTUALIZAR: SKU: {sku} ,Nombre: {nombre} , Unidad: {unidad}")
        return True

productos = Productos()
sku= input("SKU: ")
nombre = input("Nombre: ")
unidad = input("Unidad: ")

productos.insertarProducto(sku,nombre,unidad)
productos.actualizarProducto()
