# Generated by Django 4.0.4 on 2022-04-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_cd_alter_product_sd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cd',
            field=models.CharField(default='None', max_length=300, null=True),
        ),
    ]
