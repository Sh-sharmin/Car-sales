# Generated by Django 5.0.7 on 2024-12-29 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='cars/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brand.brand')),
            ],
        ),
    ]
