# Generated by Django 5.0.3 on 2024-04-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_user_github_user_phone_user_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.FileField(blank=True, upload_to='skills/'),
        ),
    ]
