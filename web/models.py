# from django.db import models
#
# class Experience(models.Model):
#     company = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#
# class Education(models.Model):
#     degree = models.CharField(max_length=100)
#     institution = models.CharField(max_length=100)
#     graduation_year = models.IntegerField()
#
# class SoftwareSkill(models.Model):
#     name = models.CharField(max_length=50)
#     proficiency_percentage = models.IntegerField()
#
# class Interest(models.Model):
#     name = models.CharField(max_length=50)
#
# class CV(models.Model):
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     about = models.TextField()
#     address = models.TextField()
#     phone = models.CharField(max_length=15)
#     email = models.EmailField()
#     facebook_link = models.URLField(blank=True, null=True)
#     github_link = models.URLField(blank=True, null=True)
#     linkedin_link = models.URLField(blank=True, null=True)
#     instagram_link = models.URLField(blank=True, null=True)
#
# class CVExperience(models.Model):
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE)
#     experience = models.ForeignKey(Experience, on_delete=models.CASCADE)
#
# class CVEducation(models.Model):
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE)
#     education = models.ForeignKey(Education, on_delete=models.CASCADE)
#
# class CVSoftwareSkill(models.Model):
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE)
#     software_skill = models.ForeignKey(SoftwareSkill, on_delete=models.CASCADE)
#
# class CVInterest(models.Model):
#     cv = models.ForeignKey(CV, on_delete=models.CASCADE)
#     interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
