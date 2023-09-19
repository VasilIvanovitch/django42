from django.db import models
from django.urls import reverse
# from django.template.defaultfilters import slugify
from pytils.translit import slugify



class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255,unique=True, db_index=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time_create']


    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)