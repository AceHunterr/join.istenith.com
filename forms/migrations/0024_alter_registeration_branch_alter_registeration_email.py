# Generated by Django 4.0.6 on 2022-08-12 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0023_formplaceholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='branch',
            field=models.CharField(choices=[('', 'Choose Your Branch'), ('Civil Engineering', 'Civil Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics And Communication Engineering', 'Electronics And Communication Engineering'), ('ECE Dual', 'ECE Dual'), ('Chemical Engineering', 'Chemical Engineering'), ('Computer Science Engineering', 'Computer Science Engineering'), ('CSE Dual', 'CSE Dual'), ('Material Science', 'Material Science'), ('Engineering Physics', 'Engineering Physics'), ('Mathematics And Computing', 'Mathematics And Computing')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Only sophomores with college email addresses are authorised.', regex='^[2][1][a-z]{3}\\d{3}@[nith.ac.in]*')]),
        ),
    ]
