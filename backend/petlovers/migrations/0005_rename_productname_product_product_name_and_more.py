# Generated by Django 4.0.4 on 2022-06-26 22:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petlovers', '0004_product_dateadded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='typeProduct',
            new_name='type_product',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='typeUser',
            new_name='type_user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='userName',
            new_name='user_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='dateAdded',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
