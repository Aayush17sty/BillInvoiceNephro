# Generated by Django 5.1.4 on 2025-01-03 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_member_bill_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='wronginvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details_received', models.BooleanField(default=False)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bill_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
    ]
