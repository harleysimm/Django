from django.shortcuts import render
from .models import Person

# Create your views here.
def v_list(request):

    consulta = Person.objects.all().order_by('firstname')

    filtro_nombre = request.GET.get("nombre", False)
    fecha_inicio = request.GET.get("startdate", None)
    fecha_fin= request.GET.get("enddate", None)

    if filtro_nombre is not False:
        consulta = consulta.filter(firstname__istartswith = filtro_nombre)

    if fecha_inicio and fecha_fin:
        consulta = consulta.filter(modifieddate__range = (fecha_inicio, fecha_fin ))

    p20 = consulta[:20]
    total_registros = p20.count()

    context = {
        'personas': p20,
        'f_firstname': filtro_nombre if filtro_nombre else '',
        'total_registros': total_registros
    }
    return render(request, 'list.html', context)

