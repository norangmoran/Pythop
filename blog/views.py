from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

# def index(request):
#     data_Post = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'DATA' : data_Post,
#         })

class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):
#     data = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'DATA' : data
#         })