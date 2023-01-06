from django.shortcuts import render, redirect
from .models import *
from django.core import serializers
from app_uas.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logoutin(request):
    logout(request)
    return redirect('login')

def halamanlogin(request):
    if request.user.is_authenticated:
        return redirect('/index')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/index')
            else:
                messages.info(request, "Username or Password is INCORRECT!")
                return render(request, "login.html")
        konteks = {
            'Title' : "Login"
        }
        return render(request, 'login.html', konteks)

def halamanregistrasi(request):
    if request.user.is_authenticated:
        return redirect('/index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')
    konteks = {
        'Title' : "Sign Up",
        'form' : form,
    }
    return render(request, 'registrasi.html', konteks)

def beranda(request):
    data_peta = lokasi.objects.all()
    penduduk = db_penduduk.objects.all()
    data_peta_json = serializers.serialize('json', data_peta)
    konteks = {
        'Title' : "Beranda",
        'datapetas' : data_peta,
        'dataJson' : data_peta_json,
        'penduduk' : penduduk,
        'judul' : "Tabel Kependudukan",
        'nama' : "Lokasi Tempat Administrasi",
    }
    print(request.user)
    return render(request, 'beranda.html', konteks)

def halamankelurahan(request):
    data_peta = lokasi.objects.all()
    denah=lokasi.objects.all()
    data_peta_json = serializers.serialize('json', data_peta)
    konteks = {
        'Title' : "Lokasi Kelurahan",
        'datapetas' : data_peta,
        'dataJson' : data_peta_json,
        'denah' : denah,
        'nama' : "Lokasi Tempat Administrasi",
        'judul' : "Tabel Tempat"
    }
    return render(request, 'kelurahan.html', konteks)

def halamankependudukan(request):
    penduduk = db_penduduk.objects.all()
    konteks = {
        'Title' : "Data Kependudukan",
        'penduduk' : penduduk,
        'judul' : "Tabel Kependudukan"
    }
    return render(request, 'kependudukan.html', konteks)

@login_required(login_url='login')
def t_lokasi(request):
    if request.POST:
        form = formlokasi(request.POST)
        if form.is_valid():
            form.save()
            form = formlokasi()
            pesan = 'Data Berhasil Ditambahkan!'    
            data = {
        'Title' : 'Tambah Data Lokasi',
        'form' : form,
        'pesan' : pesan,
     }
        return render(request, "t_lokasi.html", data)
    else:
            form = formlokasi()
            data ={
            'Title' : 'Tambah Data lokasi',
            'form' : form,}
    return render(request, "t_lokasi.html", data)

@login_required(login_url='login')
def t_kependudukan(request):
    if request.POST:
        form = formkependudukan(request.POST)
        if form.is_valid():
            form.save()
            form = formkependudukan()
            pesan = 'Data Berhasil Ditambahkan!'    
            data = {
        'Title' : 'Tambah Data Kependudukan',
        'form' : form,
        'pesan' : pesan,
     }
        return render(request, "t_kependudukan.html", data)
    else:
            form = formkependudukan()
            data ={
            'Title' : 'Tambah Data Kependudukan',
            'form' : form,}
    return render(request, "t_kependudukan.html", data)

@login_required(login_url='login')
def u_lokasi(request, id):
    denah = lokasi.objects.get(id=id)
    template = "u_lokasi.html"
    if request.POST:
        form = formlokasi(request.POST, instance=denah)
        if form.is_valid():
            form.save()
            pesan = 'Data Berhasil Diperbaharui!'    
            data = {
        'Title' : 'Perbaharui Data Lokasi',
        'form' : form,
        'pesan' : pesan,
        'Jurnal' : denah,
     
     }
        return render(request, template, data)

    else:
            form = formlokasi(instance=denah)
            data ={
            'Title' : 'Perbaharui Data Lokasi',
            'form' : form,
            'Jurnal' : denah,
    }
    return render(request, template, data)

@login_required(login_url='login')
def u_kependudukan(request, id):
    db_kependudukan = db_penduduk.objects.get(id=id)
    template = "u_kependudukan.html"
    if request.POST:
        form = formkependudukan(request.POST, instance=db_kependudukan)
        if form.is_valid():
            form.save()
            pesan = 'Data Berhasil Diperbaharui!'    
            data = {
        'Title' : 'Perbaharui Data Kependudukan',
        'form' : form,
        'pesan' : pesan,
        'Jurnal' : db_kependudukan,
     
     }
        return render(request, template, data)

    else:
            form = formkependudukan(instance=db_kependudukan)
            data ={
            'Title' : 'Perbaharui Data Kependudukan',
            'form' : form,
            'Jurnal' : db_kependudukan,
    }
    return render(request, template, data)

@login_required(login_url='login')
def d_lokasi(request, id):
    d_lokasi = lokasi.objects.filter(id = id)
    d_lokasi.delete()
    return redirect('/kelurahan/')    

@login_required(login_url='login')
def d_kependudukan(request, id):
    db_kependudukan = db_penduduk.objects.filter(id = id)
    db_kependudukan.delete()
    return redirect('/kependudukan/')    