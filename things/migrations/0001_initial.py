# Generated by Django 4.1.2 on 2022-10-11 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, max_length=120)),
                ('quantity', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
