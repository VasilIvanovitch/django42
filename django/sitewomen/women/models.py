from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator
# from django.template.defaultfilters import slugify
from pytils.translit import slugify



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            validators=[MinLengthValidator(5, message='Минимум 5 символов'),
                                        MaxLengthValidator(100, message='максимум 100 символов')])
    content = models.TextField(blank=True, verbose_name='Контент')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.PUBLISHED, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True,
                            related_name='womens', verbose_name='Категории')
    tags = models.ManyToManyField('TagPosts', blank=True, related_name='womens', verbose_name='Теги')
    husband = models.OneToOneField('Husband', on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='women', verbose_name='Муж')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['time_create']
        verbose_name = 'Знаменитые женщины'
        verbose_name_plural = 'Знаменитые женщины'


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

    class Meta:
        # ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

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
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


def read_qw(lst):
    for i, x in enumerate(lst):
        if i == 0:
            print(list(x.__dict__)[1:])
        print(list(x.__dict__.values())[1:])