# Generated by Django 5.0.6 on 2024-07-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_alter_doctor_expaties_doctor_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='amount',
            field=models.FloatField(),
        ),
    ]
