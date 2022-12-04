from django import forms
from .models import Client, Product

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'company_name': 'Empresa',
            'phone_number': 'Telefone',
            'address': 'Endereço',
            'zone': 'Zona',
            'zip_code': 'CEP',
        }
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['zone'].empty_label = 'Selecione'
        self.fields['phone_number'].help_text = 'Ex: 11 99999 9999'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'name': 'Produto',
            'price': 'Preço',
            'last_update': 'Ultima atualização'
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, *kwargs)


