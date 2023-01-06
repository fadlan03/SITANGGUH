from django.contrib import admin
from django.urls import path
from app_uas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', beranda),
    path('logout/', logoutin, name="logout"),
    path('login/', halamanlogin, name="login"),
    path('registrasi/', halamanregistrasi, name="registrasi"),
    path('kelurahan/', halamankelurahan),
    path('kelurahan/u_lokasi/<int:id>', u_lokasi, name = 'u_lokasi'),
    path('kelurahan/d_lokasi/<int:id>', d_lokasi, name = 'd_lokasi'),
    path('kependudukan/', halamankependudukan),
    path('kependudukan/u_kependudukan/<int:id>', u_kependudukan, name = 'u_kependudukan'),
    path('kependudukan/d_kependudukan/<int:id>', d_kependudukan, name = 'd_kependudukan'),
    path('tambah-kependudukan/', t_kependudukan),
    path('tambah-lokasi/', t_lokasi),
]
