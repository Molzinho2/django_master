from django.shortcuts import redirect, render
from cars.forms import CarForm, CarModelForm

from cars.models import Car

# Create your views here.
def cars(request):
    car = Car.objects.all().order_by('model') ## '-year' para ordem decrescente
    search = request.GET.get('search')

    if search:
        car = car.filter(model__icontains=search) ## '-year' para ordem decrescente
        ## constains - busca por parte do texto exato
        ## icontains - busca por parte do texto sem se importar com maiuscula e minuscula

    return render(request, 'cars.html', context={'car': car})

##def new_car_view(request):
##    
##    if request.method == 'POST':
##        new_car_form = CarForm(request.POST, request.FILES)  # Inclui request.FILES para o upload de arquivos
##        if new_car_form.is_valid():
##            new_car_form.save()
##            return redirect('cars_list')  # Redireciona para a lista de carros após o salvamento
##    else:
##        new_car_form = CarForm()
##
##    return render(request, 'new_car.html', {'new_car_form': new_car_form})

def new_car_view(request):
    
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)  # Inclui request.FILES para o upload de arquivos
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')  # Redireciona para a lista de carros após o salvamento
    else:
        new_car_form = CarModelForm()

    return render(request, 'new_car.html', {'new_car_form': new_car_form})
