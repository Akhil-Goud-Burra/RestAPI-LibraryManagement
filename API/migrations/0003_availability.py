# Generated by Django 5.0 on 2024-03-11 15:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('available_status', models.BooleanField(choices=[(True, 'Available'), (False, 'Not Available')])),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='API.book')),
            ],
        ),
    ]
