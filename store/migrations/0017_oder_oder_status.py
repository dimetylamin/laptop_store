# Generated by Django 4.0.4 on 2022-04-21 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_remove_oder_status_oder'),
    ]

    operations = [
        migrations.AddField(
            model_name='oder',
            name='oder_status',
            field=models.BooleanField(default=False),
        ),
    ]
