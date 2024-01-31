# Generated by Django 5.0.1 on 2024-01-30 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicinformation',
            old_name='email',
            new_name='cv_email',
        ),
        migrations.RenameField(
            model_name='basicinformation',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='social',
            name='dribble',
        ),
        migrations.RemoveField(
            model_name='social',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='social',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='last_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='social',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='social',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='social',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
