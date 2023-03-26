from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

# app_name = "banky_app"

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_form, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('404/', views.notFound, name='404'),
    path('about/', views.about, name='about'),
    path('services/', views.service, name='services'),
    path('details/<int:pk>', views.details, name='details'),
    path('more/', views.more, name='more'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
