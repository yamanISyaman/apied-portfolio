# Generated by Django 5.0.3 on 2024-04-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_cert_granted_on_alter_exp_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='order',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]