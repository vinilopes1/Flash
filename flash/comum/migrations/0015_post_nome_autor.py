# Generated by Django 2.0 on 2019-01-05 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0014_auto_20190105_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nome_autor',
            field=models.CharField(default='2019-01-04 15:41:46.52832-03', max_length=55, verbose_name='Nome Autor'),
            preserve_default=False,
        ),
    ]
