# Generated by Django 3.1.7 on 2021-06-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naseem', '0010_auto_20210521_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]