# Generated by Django 2.2.6 on 2019-12-09 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20191210_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='questions.Questions'),
        ),
    ]
