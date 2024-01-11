from django.db import models

class Articles (models.Model):
    title = models.CharField ( 'Title', max_length=50)
    anons = models.CharField( 'Anons', max_length=250)
    full_text = models.TextField ( 'Description')
    def __str__(self):
        return self.title
    
    class Meta:
       verbose_name='Article'
       verbose_name_plural='Articles'
# Create your models here.
