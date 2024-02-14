# Generated by Django 5.0.1 on 2024-02-03 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_education_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementAndAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='template_thumbnails/')),
                ('base', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='cover_letter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='driving_license',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='objective',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='otherskill',
            name='rating',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='industry_knowledge',
            field=models.ManyToManyField(blank=True, to='api.industryknowledge'),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='languages',
            field=models.ManyToManyField(blank=True, to='api.language'),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='other_skills',
            field=models.ManyToManyField(blank=True, to='api.otherskill'),
        ),
        migrations.AlterField(
            model_name='basicinformation',
            name='tools',
            field=models.ManyToManyField(blank=True, to='api.tool'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='designation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='industryknowledge',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='proficiency',
            field=models.CharField(blank=True, choices=[('E', 'Elementary'), ('L', 'Limited Working'), ('C', 'Conversational'), ('F', 'Fluent'), ('N', 'Native')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='otherskill',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='achievements_and_awards',
            field=models.ManyToManyField(blank=True, to='api.achievementandaward'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='activities',
            field=models.ManyToManyField(blank=True, to='api.activity'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='interests',
            field=models.ManyToManyField(blank=True, to='api.interest'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='projects',
            field=models.ManyToManyField(blank=True, to='api.project'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='publications',
            field=models.ManyToManyField(blank=True, to='api.publication'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='references',
            field=models.ManyToManyField(blank=True, to='api.reference'),
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.template'),
        ),
    ]