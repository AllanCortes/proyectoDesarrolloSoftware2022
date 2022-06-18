# Generated by Django 4.0.4 on 2022-06-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=20)),
                ('typeProduct', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('typeUser', models.CharField(max_length=20)),
            ],
        ),
    ]
