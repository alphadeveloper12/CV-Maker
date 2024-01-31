from django.contrib.auth.models import User
from django.db import models


class BasicInformation(models.Model):
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

    def __str__(self):
        return self.first_name

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

    def __str__(self):
        return self.name

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
    name = models.CharField(max_length=255 ,blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name