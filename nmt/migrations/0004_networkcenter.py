# Generated by Django 5.0.4 on 2024-05-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nmt", "0003_account_mail"),
    ]

    operations = [
        migrations.CreateModel(
            name="NetworkCenter",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nom", models.CharField(max_length=255)),
            ],
        ),
    ]
