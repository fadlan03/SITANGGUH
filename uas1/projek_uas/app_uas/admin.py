from django.contrib import admin
from .models import *
# Register your models here.

class penduduk(admin.ModelAdmin):
    list_display = ['lokasi_id', 'kk', 'jumlah_lk', 'jumlah_pr', 'total']
    search_fields = ['kk', 'jumlah_lk', 'jumlah_pr']
    list_filter = ['lokasi_id']
    list_per_page = 5
admin.site.register(lokasi)
admin.site.register(db_penduduk, penduduk)