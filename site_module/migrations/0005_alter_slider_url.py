# Generated by Django 4.1.6 on 2023-02-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_slider_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(verbose_name='لینک'),
        ),
    ]
