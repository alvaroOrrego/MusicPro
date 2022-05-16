class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True      

    def agregarCarrito(self, producto):
        id = str(producto.id_producto)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "id_producto": producto.id_producto,
                "nombre": producto.nombreProducto,
                "descripcion": producto.descripcion,
                "acumulado": producto.precio,
                "disponibilidad": producto.disponibilidad,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardarCarrito()

    def eliminarCarrito(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito:
            del self.carrito[id]
            self.guardarCarrito()

    def restart(self, producto):
        id = str(producto.id_producto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminarCarrito(producto)
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True