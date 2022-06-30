# Generated by Django 4.0.5 on 2022-06-29 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_tokenizer', '0002_alter_vehicle_reg_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
