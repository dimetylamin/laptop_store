# Generated by Django 4.0.4 on 2022-04-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
