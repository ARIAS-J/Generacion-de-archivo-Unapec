import pstats
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['file']:
#         myfiles = request.FILES['file']
        
def generar_file(request):
    response = HttpResponse(content_type='text/csv')
    
    response['Content-Disposition'] = 'attachment; filename=Pago_mensualizado.csv'
    
    lines = ["Pedrito navaja\n", "elvis tejeda"]
    response.writelines(lines)
    
    return response