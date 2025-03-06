from django.shortcuts import render

def hola_mundo(request):
    contexto = {'mensaje': 'Hola Mundo desde Django'}
    return render(request, 'index.html', contexto)

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy



class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    #context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo', 'contenido']
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
