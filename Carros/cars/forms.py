
from django import forms
from cars.models import Car, Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=200, label='Modelo')
    brand = forms.ModelChoiceField(Brand.objects.all(), label='Marca')
    factory_year = forms.IntegerField(label='Ano')
    model_year = forms.IntegerField(label='Ano do Modelo')
    plate = forms.CharField(max_length=10, label='Placa')
    value = forms.DecimalField(max_digits=10, decimal_places=2, label='Preço')
    photo = forms.ImageField(label='Imagem', required=False)  # Campo de imagem opcional

    def save(self):
        # Aqui você pode implementar a lógica para salvar o carro no banco de dados
        # Por exemplo:
        car = Car(
            model=self.cleaned_data['model'],
            brand=self.cleaned_data['brand'],
            factory_year=self.cleaned_data['factory_year'],
            model_year=self.cleaned_data['model_year'],
            plate=self.cleaned_data['plate'],
            value=self.cleaned_data['value'],
            photo=self.cleaned_data['photo']
        )
        car.save()

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'  # Inclui todos os campos do modelo Car

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'O valor mínimo do carro deve ser maior que R$ 20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano de fabricação deve ser maior que 2000')
        return factory_year