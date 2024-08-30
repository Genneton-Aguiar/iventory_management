from django.db import models
from django.contrib.auth.models import User

from django.db.models import TextChoices

class MovementChoices(TextChoices):
    IN = 'IN', 'Entrada'
    OUT = 'OUT', 'Saída'
    
    
    
class Product(models.Model):    

    name = models.CharField(
        max_length=255
    )
    
    description = models.CharField(
        max_length=255
    )

    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2
        )
    
    category = models.CharField(
        max_length=255,
    )
    
    code= models.CharField(
        verbose_name='codigo do produto',
        max_length=255
    )
    
    avaliable= models.BooleanField(
        default=True
    )   
    
    removed= models.BooleanField(
        default=False
    )

    sotck_quantiy=models.PositiveIntegerField(
        default='0'
    )

class Movements (models.Model):
    
    IN= 'IN'
    OUT= 'OUT'
    TYPE_CHOICES=(
        (IN,'IN'),
        (OUT,'OUT')
    )
    
    amount = models.IntegerField(
        verbose_name="Quantidade",
        blank=False,
        null=False
    )
    
    product=models.ForeignKey(
       Product,
       verbose_name='id do produto',
       on_delete=models.DO_NOTHING
   )
    
    reason = models.CharField(
        verbose_name='motivo da movimentação',
        max_length=255
    )
    
    movement_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    
    date= models.DateField(
        verbose_name='data da movimentação',
        blank=True,
        null=True
    )
    
    user = models.ForeignKey(
        User,
        verbose_name='usuario',
        on_delete=models.DO_NOTHING,
        default=''
    )
    
