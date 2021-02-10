from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog

# Create your views here.


class index(ListView):
    model = Blog
    ordering = ['-id']


class detail(DetailView):
    model = Blog


class create(CreateView):
    model = Blog
    fields = ['title', 'content']
    success_url = '/blog/'


class update(UpdateView):
    model = Blog
    fields = ['title', 'content']
    success_url = '/blog/'


class delete(DeleteView):
    model = Blog
    success_url = '/blog/'


def search(request):
    queryset = Blog.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(content__icontains=keywords)

    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset = queryset.filter(title__iexact=title)

    context = {
        'query': queryset,
    }

    return render(request, 'blog/search.html', context)
