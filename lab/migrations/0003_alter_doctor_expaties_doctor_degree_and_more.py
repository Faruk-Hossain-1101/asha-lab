# Generated by Django 5.0.6 on 2024-07-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='expaties',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='degree',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='DoctorExpaties',
        ),
    ]
