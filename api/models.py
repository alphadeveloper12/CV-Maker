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
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    cv_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    industry_knowledge = models.ManyToManyField('IndustryKnowledge', blank=True)
    tools = models.ManyToManyField('Tool', blank=True)
    other_skills = models.ManyToManyField('OtherSkill', blank=True)
    languages = models.ManyToManyField('Language', blank=True)
    social = models.JSONField(default=dict, blank=True, null=True)
    educations = models.ManyToManyField('Education', blank=True)
    experiences = models.ManyToManyField('Experience', blank=True)
    objective = models.CharField(max_length=1000, null=True, blank=True)
    projects = models.ManyToManyField('Project', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, null=True, blank=True)
    driving_license = models.CharField(max_length=20, null=True, blank=True)
    interests = models.ManyToManyField('Interest', blank=True)
    activities = models.ManyToManyField('Activity', blank=True)
    website = models.URLField(blank=True, null=True)
    achievements_and_awards = models.ManyToManyField('AchievementAndAward', blank=True)
    publications = models.ManyToManyField('Publication', blank=True)
    cover_letter = models.TextField(null=True, blank=True)
    references = models.ManyToManyField('Reference', blank=True)
    additional_info = models.TextField(null=True, blank=True)
    template = models.ManyToManyField(Template)

    def __str__(self):
        # if self.template:
        #     return f"CV: {self.first_name} - Template: {self.template.title}"
        # else:
        #     return f"{self.first_name}"
        return f"{self.first_name}"


class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Interest(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name


class AchievementAndAward(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reference(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    designation = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    start_at = models.DateField(null=True, blank=True)
    end_at = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class Education(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(default=None, blank=True, null=True)
    location = models.TextField(null=True, blank=True)
    start_at = models.DateField(null=True, blank=True)
    end_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class IndustryKnowledge(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.name


class OtherSkill(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 5)], null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Rating: {self.rating}"


class Language(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    proficiency_choices = [
        ('E', 'Elementary'),
        ('L', 'Limited Working'),
        ('C', 'Conversational'),
        ('F', 'Fluent'),
        ('N', 'Native'),
    ]
    proficiency = models.CharField(max_length=1, choices=proficiency_choices,null=True, blank=True)

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
