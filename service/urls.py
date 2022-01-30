from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("reports/", ReportListView.as_view(), name="reports"),


]
