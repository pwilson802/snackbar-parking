# Generated by Django 3.0.1 on 2020-01-23 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200120_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_id',
            field=models.CharField(default='temp', max_length=100),
            preserve_default=False,
        ),
    ]
