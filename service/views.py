from django.shortcuts import render
from .forms import PostForm
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


def index(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})

    else:
        form = PostForm()
    return render(request, 'index.html', {'form': form, 'index': index})


class ReportListView(ListView):
    model = Post
    template_name = "Report.html"
    context_object_name = "reports"


class SearchViewSet(ModelViewSet):
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['pin']
    search_fields = ['pin', 'name', 'surname', 'patronymic']
    ordering_fields = ['pin', 'name', 'surname', 'patronymic']
    template_name = "Report.html"
    context_object_name = "reports"
