# Generated by Django 4.2.1 on 2023-06-05 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaukos',
            name='grade',
            field=models.CharField(default='hey?', max_length=50),
        ),
    ]