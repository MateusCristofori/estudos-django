# Generated by Django 4.0.6 on 2022-07-11 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(default=1, auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('data_receita', models.DateTimeField(
                    blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
