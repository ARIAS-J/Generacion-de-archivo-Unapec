import pstats
from django.shortcuts import render
from django.http import HttpResponse

from app.models import Nomina

# Create your views here.

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         myfiles = request.FILES['file']

def home(request):
    
    return render(request, 'app/home.html')

def generar_file(request):
    response = HttpResponse(content_type='text/csv')
    
    response['Content-Disposition'] = 'attachment; filename=Pago_mensualizado.csv'
    
    separador = "|"
    contador = 0
    
    rnc = "123456789"
    cuenta = "12345678911"
    fecha = "26/05/2022"
    
    nominas = Nomina.objects.all()
    
    lines = []
    
    lines.append(f'SEP={separador}\n')
    lines.append(f'E{separador}{rnc}{separador}{cuenta}{separador}{fecha}{separador}\n')
    
    for nomina in nominas:
        lines.append(f'D{separador}{nomina.cedula}{separador}{nomina.nombre}{separador}{nomina.primer_apellido}{separador}{nomina.segundo_apellido}{separador}{nomina.puesto_trabajo}{separador}{nomina.numero_cuenta}{separador}{nomina.monto_pagar}\n')
        contador += 1
    
    lines.append(f'S{separador}{contador}\n')
    
    response.writelines(lines)
    
    return response