# Generated by Django 2.2.7 on 2019-12-17 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_categoty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoty',
            new_name='category',
        ),
    ]