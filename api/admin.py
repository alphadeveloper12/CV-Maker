# admin.py

from django.contrib import admin
from .models import BasicInformation, Experience, Education, IndustryKnowledge, Tool, OtherSkill, Language, Social



admin.site.register(BasicInformation)
admin.site.register(IndustryKnowledge)
admin.site.register(Tool)
admin.site.register(OtherSkill)
admin.site.register(Language)
admin.site.register(Social)
admin.site.register(Experience)
admin.site.register(Education)
