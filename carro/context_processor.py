

from carro.carro import Carro

def importe_total_carro(request):

    carro=Carro(request)

    total=0

 
    for key, value in request.session["carro"].items():
        total=total+(float(value["precio"])*1)

    return {"importe_total_carro":total}





def cantidad_proce(request):

    carro=Carro(request)

    canti=0

    for key, value in request.session["carro"].items():

        canti=canti + value["cantidad"]


    return  {"cantidad_proce":canti}




def cantidad_desti(request):

    carro=Carro(request)

    desti=""

    for key, value in request.session["carro"].items():

        desti=desti + value["destino"]


    return  {"cantidad_desti":desti}
