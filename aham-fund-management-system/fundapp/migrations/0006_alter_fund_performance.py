# Generated by Django 5.2 on 2025-04-21 01:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundapp', '0005_alter_fund_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='performance',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
