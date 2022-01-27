from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'pin', 'plot', 'image', 'image1', 'image2')



