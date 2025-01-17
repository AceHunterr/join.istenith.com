# Generated by Django 4.0.7 on 2022-11-26 20:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Only freshers with college email addresses are authorised.', regex='^[2][2][a-z]{3}\\d{3}@[nith.ac.in]*')]),
        ),
    ]
