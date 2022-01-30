from django.shortcuts import render
from .forms import PostForm
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


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




