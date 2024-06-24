from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    lesson_name = models.CharField(verbose_name="Dars nomi", max_length=255)
    lesson_number = models.CharField(verbose_name="Dars Soni", max_length=255)
    videoId = models.CharField(verbose_name="VideoId" , max_length=255)
    description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=False)
    telegram = models.CharField(verbose_name="Telegram man'ba", max_length=255, null=False)
    youtube = models.CharField(verbose_name="Youtube man'ba", max_length=255, null=False)

    # category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=20) 
    category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)
    # subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=20)
    subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)

    def __str__(self):
        return f"№{self.id} - {self.lesson_name}"
