from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path("reports/", ReportListView.as_view(), name="reports"),
    path("search-photo/", SearchListView.as_view(), name="search_photo"),


]
