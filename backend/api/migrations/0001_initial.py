# Generated by Django 4.0.7 on 2022-08-31 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('imageUrl', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
