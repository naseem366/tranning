# Generated by Django 3.1.7 on 2021-05-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naseem', '0004_auto_20210512_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='region',
        ),
    ]