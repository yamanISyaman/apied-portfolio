# Generated by Django 5.0.3 on 2024-04-19 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_skill_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='order',
            field=models.BigIntegerField(unique=True),
        ),
    ]
