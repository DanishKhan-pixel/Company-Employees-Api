# Generated by Django 5.0.4 on 2024-04-29 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('name', 'alpha'), ('location', 'islamabad'), ('about', 'about ')], max_length=100)),
                ('add_date', models.DateField(auto_now=True)),
                ('activa', models.BooleanField(default=True)),
            ],
        ),
    ]
