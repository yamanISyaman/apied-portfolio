# Generated by Django 5.0.3 on 2024-04-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_skill_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
