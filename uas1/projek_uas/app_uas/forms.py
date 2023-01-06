from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app_uas.models import *

class formlokasi(ModelForm):
    class Meta:
        model = lokasi
        fields = '__all__'

        widgets = {
      'nama_lokasi' : forms.TextInput({'class':'form-control'}),
      'garis_lintang' : forms.TextInput({'class':'form-control'}),
      'garisbujur' : forms.TextInput({'class':'form-control'}),
      'alamat' : forms.TextInput({'class':'form-control'}),
    }

class formkependudukan(ModelForm):
    class Meta:
        model = db_penduduk
        fields = '__all__'

        widgets = {
      'kk' : forms.TextInput({'class':'form-control'}),
      'jumlah_lk' : forms.TextInput({'class':'form-control'}),
      'jumlah_pr' : forms.TextInput({'class':'form-control'}),
      'total' : forms.TextInput({'class':'form-control'}),
      'lokasi_id' : forms.Select({'class':'form-control'}),
    }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
