# Generated by Django 4.0.6 on 2022-08-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название статьи'),
        ),
    ]
