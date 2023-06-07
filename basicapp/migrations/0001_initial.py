# Generated by Django 4.2.1 on 2023-06-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chaukos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('woodName', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FurnitureItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=1)),
                ('price', models.IntegerField()),
                ('des', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ModularItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=1)),
                ('des', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
    ]