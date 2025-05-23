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