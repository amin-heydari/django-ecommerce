# Generated by Django 4.1.6 on 2023-03-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]
