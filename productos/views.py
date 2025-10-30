from django.shortcuts import render

from productos.models import Producto

def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarListado(request):
     pro =Producto.objects.all().values()
     datos = {'pro' : pro}
     return render(request, 'listado.html', datos)

def mostrarform_registrar(request):
    return render(request, 'form_registrar.html')

def mostrarform_actualizar(request, id):
    try:
        pro =Producto.objects.get(id = id)
        datos = {'pro' : pro}
        return render(request, 'form_actualizar.html',datos)
    except:
        pro =Producto.objects.all().values()
        datos = {'pro' : pro,
                 'r2' : 'El ID ('+ str(id)+') No es posible Actualizar'}
        return render(request, 'listado.html', datos)

def Insertar_producto(request):
    if request.method =='POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        cos = request.POST['txtcos']
        fec = request.POST['txtfec']
        pzas = request.POST['txtpzas']
        act = request.POST['radact']
        cat = request.POST['txtcat']
        des =request.POST['txtdes']
        pizmin =request.POST['txtpizmin']
        ubi = request.POST['txtubi']
        pro = Producto(nombre = nom,marca=mar, costo=cos,piezas=pzas, fec_ing= fec, activo=act, categoria= cat, descuento=des, stock_minimo=pizmin, ubicacion = ubi)
        pro.save()
        datos = {'r' : "Registro se Inserto de forma correta"}
        return render(request, 'form_registrar.html',datos)
    else:
        datos = {'r2' : "No se Puede Procesar Solicitud"}
        return render(request, 'form_registrar.html',datos)
    
def actualizar_producto(request, id ):
    if request.method =='POST':
        nom = request.POST['txtnom']
        mar = request.POST['cbomar']
        cos = request.POST['txtcos']
        fec = request.POST['txtfec']
        pzas = request.POST['txtpzas']
        act = request.POST['radact']
        cat = request.POST['txtcat']
        des =request.POST['txtdes']
        pizmin =request.POST['txtpizmin']
        ubi = request.POST['txtubi']
        pro = Producto.objects.get(id = id)
        pro.nombre = nom
        pro.marca=mar
        pro.precio=cos
        pro.piezas=pzas
        pro.fec_ing= fec
        pro.activo=act
        pro.categoria=cat
        pro.descuento=des
        pro.stock_minimo=pizmin
        pro.ubicacion = ubi
        pro.save()
        pro =Producto.objects.all().values()
        datos = {'pro' : pro,
                 'r' : "Se Actualizaron los datos de forma correta"}
        return render(request, 'listado.html',datos)
    else:
        datos = {'r2' : "No se Puede Procesar Solicitud"}
        return render(request, 'listado.html',datos)

def eliminar_producto (request, id ):
    try:
        pro =Producto.objects.get(id = id)
        pro.delete()
        pro =Producto.objects.all().values()
        datos = {'pro' : pro,
                 'r' : "Se Borraron los datos de forma correta"}
        return render(request, 'listado.html',datos)
    except:
        pro =Producto.objects.all().values()
        datos = {'pro' : pro,
                 'r2' : 'El ID ('+ str(id)+') No es posible Actualizar'}
        return render(request, 'listado.html', datos)