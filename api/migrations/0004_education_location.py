# Generated by Django 5.0.1 on 2024-01-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_experience_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='location',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
