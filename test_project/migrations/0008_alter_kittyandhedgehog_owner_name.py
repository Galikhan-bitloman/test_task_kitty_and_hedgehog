# Generated by Django 4.0.2 on 2022-02-09 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_project', '0007_alter_kittyandhedgehog_owner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kittyandhedgehog',
            name='owner_name',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
