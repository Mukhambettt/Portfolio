from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    msg = models.TextField(verbose_name='Сообщение')
    dateTime = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'Вы получили сообщение: {self.name} | {self.email}'
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'