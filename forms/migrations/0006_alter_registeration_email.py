# Generated by Django 4.0.8 on 2022-12-05 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_alter_registeration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Only freshers with correct college email addresses are authorised.', regex='^[2][2][a-zA-Z]{3}\\d{3}@nith[.]ac[.]in$')]),
        ),
    ]
