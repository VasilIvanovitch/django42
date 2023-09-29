from django.db import models
from django.urls import reverse
# from django.template.defaultfilters import slugify
from pytils.translit import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='womens')
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='womens')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='women')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time_create']


    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_slug': self.slug})
        # return reverse('women:post', args=(self.slug,))


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name}: {self.pk}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)



    def get_absolute_url(self):
        return reverse('women:category', kwargs={'cat_slug': self.slug})


class TagPosts(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('women:tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(null=True, verbose_name='Возраст')

    def __str__(self):
        return self.name

