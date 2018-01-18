from django.forms import ModelForm
from weblab.models import *

class AddUslugaForm(ModelForm):
    class Meta:
        model = Uslugi
        fields = ['name', 'price', 'meta_opis', 'image']
        labels = {
            'name' : 'Название',
            'price' : 'Цена',
            'meta_opis' : 'Описание',
            'image' : 'Картинка'
        }
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            'name' : 'Ваше имя',
            'email' : 'Ваш email',
            'message' : 'Сообщение'
        }