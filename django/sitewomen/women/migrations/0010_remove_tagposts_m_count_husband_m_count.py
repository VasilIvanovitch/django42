# Generated by Django 4.2.5 on 2023-09-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0009_alter_women_options_tagposts_m_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tagposts',
            name='m_count',
        ),
        migrations.AddField(
            model_name='husband',
            name='m_count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
