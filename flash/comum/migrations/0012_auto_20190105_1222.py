# Generated by Django 2.0 on 2019-01-05 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0011_auto_20190105_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor', to='comum.Perfil'),
        ),
    ]
