from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('surname', 'name', 'patronymic', 'pin', 'address', 'plot', 'image', 'image1', 'image2')
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

            "plot": forms.Textarea(
                attrs={"class": "form-control",
                       "placeholder": "Фабула",
                        "rows": 5,
                       }),
            "image": forms.FileInput(
                attrs={"class": "form-control",

                       "placeholder": "Фото",


                       }),
            "image1": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фото",
                       "id": "imgInp",
                       "type": "file",
                       }),
            "image2": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "Фото"
                       }),

        }
# <img id="face-preview" class="img-thumbnail d-block"
# style="display: block; margin-left: auto; margin-right: auto;"
# src="//search4faces.com/img/user-placeholder.jpg" alt="placeholder">