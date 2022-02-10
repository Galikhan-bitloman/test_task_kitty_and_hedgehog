# Generated by Django 4.0.2 on 2022-02-05 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0003_user_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select_bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_of_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_project.bet')),
                ('user_who_make_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_project.user')),
            ],
        ),
    ]