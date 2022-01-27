from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('reports/', report, name='reports'),
    path('registre', registr, name='registre'),

]
