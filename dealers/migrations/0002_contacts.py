# Generated by Django 5.0.4 on 2024-04-13 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.TextField(verbose_name='Город')),
                ('street', models.TextField(verbose_name='Улица')),
                ('house_number', models.PositiveSmallIntegerField(verbose_name='Номер дома')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dealers.countries', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
