from django.db import models


# Create your models here.

class Noticia(models.Model):
    class Meta:
        verbose_name = u'Noticia'
        verbose_name_plural = u'Noticias'

    assunto = models.CharField(u"Assunto", null=False, blank=False, max_length=255)
    news = models.TextField(u'Noticia', null=False, blank=False)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.assunto