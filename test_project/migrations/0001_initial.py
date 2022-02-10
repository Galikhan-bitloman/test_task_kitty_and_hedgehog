# Generated by Django 4.0.2 on 2022-02-02 17:29

from django.db import migrations, models
import test_project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bet', models.IntegerField(default=0)),
                ('onwer_name', models.CharField(max_length=100, verbose_name=test_project.models.User)),
            ],
        ),
        migrations.CreateModel(
            name='KittyandHedgehog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100, verbose_name=test_project.models.User)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=test_project.models.KittyandHedgehog)),
                ('price', models.IntegerField(default=0)),
                ('owner_name', models.CharField(max_length=100, verbose_name=test_project.models.User)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_money', models.IntegerField(default=0)),
            ],
        ),
    ]