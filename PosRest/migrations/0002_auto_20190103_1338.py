# Generated by Django 2.1.4 on 2019-01-03 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PosRest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
