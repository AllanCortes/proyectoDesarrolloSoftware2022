# Generated by Django 4.0.4 on 2022-06-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petlovers', '0002_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
