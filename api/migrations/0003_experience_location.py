# Generated by Django 5.0.1 on 2024-01-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_email_basicinformation_cv_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
