
class Carro:


    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}

        self.carro=carro
    

    def agregar(self, producto):

        if (producto.destino) not in self.carro.keys():

            self.carro[producto.destino]={

                "destino":producto.destino,
                "precio":str(producto.precio),
                "cantidad":1,
                "foto":producto.foto.url,

            }

        else:

            for key, value in self.carro.items():

                if key ==producto.destino:

                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+ producto.precio
                    break

        self.guardar_carro()


    def guardar_carro(self):


        self.session["carro"]=self.carro
        self.session.modified=True


    def eliminar(self, producto):

        producto.destino=producto.destino
        if producto.destino in self.carro:
            del self.carro[producto.destino]
            self.guardar_carro()


    def restar(self, producto):

        for key, value in self.carro.items():

                if key==producto.destino:

                    value["cantidad"]=value["cantidad"]-1
                    value["precio"]=float(value["precio"])- producto.precio
                    if value["cantidad"]<1:
                        self.eliminar(producto)

                    break

        self.guardar_carro()


    def limpiar(self):
        carro=self.session["carro"]={}
        self.session.modified=True

        



    





