# Generated by Django 4.0.4 on 2022-04-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_product_name_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='newprice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='laptop/'),
        ),
    ]