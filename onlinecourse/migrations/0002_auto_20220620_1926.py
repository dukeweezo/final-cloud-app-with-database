# Generated by Django 3.1.3 on 2022-06-20 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_grade',
            field=models.FloatField(default=1.0),
        ),
    ]
