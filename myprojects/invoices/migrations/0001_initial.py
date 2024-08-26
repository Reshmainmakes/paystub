# Generated by Django 4.2.15 on 2024-08-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('regular_hour_rate', models.DecimalField(decimal_places=2, default=12.0, max_digits=5)),
                ('overtime_hour_rate', models.DecimalField(decimal_places=2, default=18.0, max_digits=5)),
                ('week1_regular_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week1_overtime_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week2_regular_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week2_overtime_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week3_regular_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week3_overtime_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week4_regular_hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('week4_overtime_hours', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
