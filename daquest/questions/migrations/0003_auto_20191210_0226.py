# Generated by Django 2.2.6 on 2019-12-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20191210_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
