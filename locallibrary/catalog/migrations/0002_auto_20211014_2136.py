# Generated by Django 3.2.8 on 2021-10-15 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='atm_number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='atm',
            name='current_balance',
            field=models.IntegerField(default=100),
        ),
    ]
