# Generated by Django 4.0.4 on 2022-06-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petlovers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]