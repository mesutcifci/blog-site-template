# Generated by Django 3.1.4 on 2021-01-07 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20201219_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=models.FileField(upload_to='article_image/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg'])]),
        ),
    ]
