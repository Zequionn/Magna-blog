from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>', views.post, name="post"),
    path('form_post/', views.form, name="form"),
    path('delete_post/<str:pk>', views.deletePost, name="delete_post"),
    path('update_post/<str:pk>', views.update_post, name="update_post"),
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html', next_page='home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]