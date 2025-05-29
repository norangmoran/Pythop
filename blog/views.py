from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    data_Post = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'DATA' : data_Post,
        })

def single_post_page(request, pk):
    data = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'DATA' : data
        })