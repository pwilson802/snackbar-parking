# Generated by Django 2.2.7 on 2019-12-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_byline'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoty',
            field=models.CharField(default='park', max_length=30),
            preserve_default=False,
        ),
    ]
