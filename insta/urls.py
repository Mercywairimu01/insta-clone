from django.contrib.auth import views as auth_views
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('', PostListView.as_view(),name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name ='post_detail.html'), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name ='post_form.html'), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name ='post_form.html'), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name ='post_confirm_delete.html'), name='post-delete'),
    path('register/',views.register,name ='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name ='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name ='logout'),
    path('profile/',views.profile,name ='profile'),
    path('search/', views.SearchResults, name='search_results'),
]