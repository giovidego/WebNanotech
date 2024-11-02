class Carro:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro = self.session.get("carro")
        # if 'carro' not in request.session:
        # # Si no existe, inicialízalo como un diccionario vacío
        # request.session['carro'] = {}
        if not carro:
            carro=self.session["carro"]={}
        
        self.carro=carro

    def existe(self, producto):
        
        return str(producto.sku) in self.carro
    
    def actualizar(self, producto, cantidad):
        
        if self.existe(producto):
            self.carro[str(producto.sku)]['cantidad'] += cantidad
    
    def agregar(self, producto, cantidad_producto):
                              
            producto_id = str(producto.sku)
           
            if producto_id not in self.carro:
                sub = int(producto.precio) * int(cantidad_producto)
                
                self.carro[producto_id] = {
                'sku': producto.sku,
                'foto': producto.foto.url,
                'marca': producto.marca,
                'nombre': producto.nombre,
                'cantidad': cantidad_producto,
                'precio': producto.precio,
                'subtotal': sub
                
                
        }
            else:
                for key, value in self.carro.items():
                    if key == producto_id:
                        value['cantidad']= int(value['cantidad'])+1
                        value['subtotal']= int(value['subtotal']) * value['cantidad']
                        break
            self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, producto):
        producto_id = str(producto.sku)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()
            self.session.modified = True

    def restar_producto(self, producto):
        for key, value in self.carro.items():
            if key == str(producto.sku):
                value["cantidad"]=int(value["cantidad"])-1
                value["subtotal"]= int(value["subtotal"])- producto.precio
                if value["cantidad"]<1:
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    def sumar_producto(self, producto):
        producto_id = str(producto.sku)
        for key, value in self.carro.items():
            if key == producto_id:
                value['cantidad']= int(value['cantidad'])+1
                value['subtotal']= int(value['subtotal']) + value['precio']
                break
        self.guardar_carro()


    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True