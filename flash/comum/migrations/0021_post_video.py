# Generated by Django 2.0 on 2019-01-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0020_auto_20190108_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='arquivos/%Y/posts/', verbose_name='Foto'),
        ),
    ]
