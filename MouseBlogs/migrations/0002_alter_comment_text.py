# Generated by Django 3.2 on 2021-04-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MouseBlogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=50),
        ),
    ]
