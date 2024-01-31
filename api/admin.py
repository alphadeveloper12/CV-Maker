# admin.py

from django.contrib import admin
from .models import BasicInformation, Experience, Education, IndustryKnowledge, Tool, OtherSkill, Language, Social, Template, Project, Interest, Activity, AchievementAndAward, Publication, Reference


admin.site.register(BasicInformation)
admin.site.register(IndustryKnowledge)
admin.site.register(Tool)
admin.site.register(OtherSkill)
admin.site.register(Language)
admin.site.register(Social)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Template)
admin.site.register(Project)
admin.site.register(Interest)
admin.site.register(Activity)
admin.site.register(AchievementAndAward)
admin.site.register(Publication)
admin.site.register(Reference)
