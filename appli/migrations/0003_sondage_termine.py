# Generated by Django 3.1.2 on 2020-10-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0002_auto_20201020_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='sondage',
            name='termine',
            field=models.BooleanField(null=True),
        ),
    ]
