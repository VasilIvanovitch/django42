# Generated by Django 4.2.5 on 2023-11-08 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('women', '0011_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
