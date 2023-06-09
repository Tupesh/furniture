# Generated by Django 4.2.1 on 2023-06-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0008_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='contact_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='district',
            field=models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Bhaktapur', 'Bhaktapur'), ('Lalitpur', 'Lalitpur')], max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
