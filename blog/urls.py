from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Importa las vistas de autenticación
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostList


urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('api/posts/', PostList.as_view(), name='api_post_list'),
    path('login/', LoginView.as_view(template_name='login.html', next_page='post_list'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]