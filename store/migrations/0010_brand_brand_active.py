# Generated by Django 4.0.4 on 2022-04-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_cd_alter_product_sd'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_active',
            field=models.BooleanField(default=False),
        ),
    ]
