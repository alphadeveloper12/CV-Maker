from django.contrib.auth.models import User
from django.db import models


class Template(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='template_thumbnails/', blank=True, null=True)
    base = models.TextField()
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BasicInformation(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    cv_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    industry_knowledge = models.ManyToManyField('IndustryKnowledge')
    tools = models.ManyToManyField('Tool')
    other_skills = models.ManyToManyField('OtherSkill')
    languages = models.ManyToManyField('Language')
    social = models.JSONField(default=dict, blank=True, null=True)
    educations = models.ManyToManyField('Education', blank=True)
    experiences = models.ManyToManyField('Experience', blank=True)
    objective = models.CharField(max_length=1000)
    projects = models.ManyToManyField('Project', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    driving_license = models.CharField(max_length=20)
    interests = models.ManyToManyField('Interest', blank=True)
    activities = models.ManyToManyField('Activity', blank=True)
    website = models.URLField(blank=True)
    achievements_and_awards = models.ManyToManyField('AchievementAndAward', blank=True)
    publications = models.ManyToManyField('Publication', blank=True)
    cover_letter = models.TextField()
    references = models.ManyToManyField('Reference', blank=True)
    additional_info = models.TextField()
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.template:
            return f"CV: {self.first_name} - Template: {self.template.title}"
        else:
            return f"{self.first_name}"


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Interest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AchievementAndAward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Experience(models.Model):
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    start_at = models.DateField()
    end_at = models.DateField()
    description = models.TextField()
    location = models.TextField()

    def __str__(self):
        return self.company_name


class Education(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    icon = models.ImageField(default=None, blank=True, null=True)
    location = models.TextField()
    start_at = models.DateField()
    end_at = models.DateField()

    def __str__(self):
        return self.name


class IndustryKnowledge(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class OtherSkill(models.Model):
    name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.name} - Rating: {self.rating}"


class Language(models.Model):
    name = models.CharField(max_length=255)
    proficiency_choices = [
        ('N', 'Native'),
        ('P', 'Professional'),
    ]
    proficiency = models.CharField(max_length=1, choices=proficiency_choices)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=255, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
