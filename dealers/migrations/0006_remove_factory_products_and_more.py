# Generated by Django 5.0.4 on 2024-04-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealers', '0005_alter_factory_debt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factory',
            name='products',
        ),
        migrations.RemoveField(
            model_name='individualentrepreneur',
            name='products',
        ),
        migrations.RemoveField(
            model_name='retailnetwork',
            name='products',
        ),
        migrations.AddField(
            model_name='factory',
            name='products',
            field=models.ManyToManyField(to='dealers.products', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='individualentrepreneur',
            name='products',
            field=models.ManyToManyField(to='dealers.products', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='retailnetwork',
            name='products',
            field=models.ManyToManyField(to='dealers.products', verbose_name='Продукты'),
        ),
    ]
