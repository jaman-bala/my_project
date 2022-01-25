from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('surname', 'name', 'patronymic', 'pin', 'plot', 'image', 'image1', 'image2')
        widgets = {

            "surname": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Фамилия"
                       }),
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Имя"
                       }),
            "patronymic": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Отчество"
                       }),
            "pin": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "ПИН"
                       }),
            "address": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Адрес"
                       }),
            "plot": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Фабула"
                       }),
            "image": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Фото"
                       }),
            "image1": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фото"
                       }),
            "image2": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фото"
                       }),

        }
# image = forms.URLField(required=True,
#                        label=False,
#                        widget=forms.TextInput(
#                         attrs={'placeholder': 'add image'}))