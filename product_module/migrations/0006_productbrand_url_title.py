# Generated by Django 4.1.6 on 2023-03-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url_title', max_length=300, verbose_name='نام در url'),
            preserve_default=False,
        ),
    ]
