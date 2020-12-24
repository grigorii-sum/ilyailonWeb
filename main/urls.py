from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('', views.welcome_page, name='welcome'),
    path('blog-of-ilyailon', views.blog_page, name='blog'),
    path('post_of_dogs', views.dog_post_page, name='dogs'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
