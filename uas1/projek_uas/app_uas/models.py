from django.db import models

# Create your models here.
class lokasi(models.Model):
    nama_tempat = models.CharField(max_length=100)
    garis_lintang = models.CharField(max_length=150)
    garisbujur = models.CharField(max_length=100,default='' )
    alamat = models.CharField(max_length=250)

    def __str__(self):
        return self.nama_tempat

class db_penduduk(models.Model):
    lokasi_id = models.ForeignKey(lokasi, on_delete=models.CASCADE, null=True)
    kk = models.CharField(max_length=50)
    jumlah_lk = models.CharField(max_length=50)
    jumlah_pr = models.CharField(max_length=50)
    total = models.CharField(max_length=50)

    def __str__(self):
        return self.kk

