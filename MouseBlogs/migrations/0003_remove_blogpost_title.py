# Generated by Django 3.2 on 2021-04-30 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MouseBlogs', '0002_alter_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='title',
        ),
    ]
