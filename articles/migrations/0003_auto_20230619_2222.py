# Generated by Django 3.1.2 on 2023-06-19 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230618_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название статьи'),
        ),
    ]