# Generated by Django 5.2.1 on 2025-07-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churras', '0003_prato_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='foto_prato',
            field=models.ImageField(blank=True, upload_to='pratos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='prato',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
