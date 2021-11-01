# Generated by Django 3.2.8 on 2021-11-01 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('registry', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('length', models.IntegerField()),
            ],
        ),
    ]