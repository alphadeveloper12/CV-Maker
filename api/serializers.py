# api/serializers.py

from rest_framework import serializers
from .models import *


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class OtherSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSkill
        fields = '__all__'


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'


class IndustryKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryKnowledge
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class AchievementAndAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementAndAward
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password',)


class BasicInformationSerializer(serializers.ModelSerializer):
    social = SocialSerializer(allow_null=True, required=False)
    languages = LanguageSerializer(many=True, allow_null=True, required=False)
    other_skills = OtherSkillSerializer(many=True, allow_null=True, required=False)
    tools = ToolSerializer(many=True, allow_null=True, required=False)
    industry_knowledge = IndustryKnowledgeSerializer(many=True, allow_null=True, required=False)
    educations = EducationSerializer(many=True, allow_null=True, required=False)
    experiences = ExperienceSerializer(many=True, allow_null=True, required=False)
    projects = ProjectSerializer(many=True, allow_null=True, required=False)
    interests = InterestSerializer(many=True, allow_null=True, required=False)
    activities = ActivitySerializer(many=True, allow_null=True, required=False)
    achievements_and_awards = AchievementAndAwardSerializer(many=True, allow_null=True, required=False)
    publications = PublicationSerializer(many=True, allow_null=True, required=False)
    references = ReferenceSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = BasicInformation
        fields = '__all__'

    def create(self, validated_data):
        industry_knowledge_data = validated_data.pop('industry_knowledge', [])
        tools_data = validated_data.pop('tools', [])
        other_skills_data = validated_data.pop('other_skills', [])
        languages_data = validated_data.pop('languages', [])
        educations_data = validated_data.pop('educations', [])
        experiences_data = validated_data.pop('experiences', [])
        projects_data = validated_data.pop('projects', [])
        interests_data = validated_data.pop('interests', [])
        activities_data = validated_data.pop('activities', [])
        achievements_and_awards_data = validated_data.pop('achievements_and_awards', [])
        publications_data = validated_data.pop('publications', [])
        references_data = validated_data.pop('references', [])

        basic_info = BasicInformation.objects.create(**validated_data)

        # Create and associate related objects
        basic_info.industry_knowledge.set(IndustryKnowledge.objects.create(**item) for item in industry_knowledge_data)
        basic_info.tools.set(Tool.objects.create(**item) for item in tools_data)
        basic_info.other_skills.set(OtherSkill.objects.create(**item) for item in other_skills_data)
        basic_info.languages.set(Language.objects.create(**item) for item in languages_data)
        basic_info.educations.set(Education.objects.create(**item) for item in educations_data)
        basic_info.experiences.set(Experience.objects.create(**item) for item in experiences_data)
        basic_info.projects.set(Project.objects.create(**item) for item in projects_data)
        basic_info.interests.set(Interest.objects.create(**item) for item in interests_data)
        basic_info.activities.set(Activity.objects.create(**item) for item in activities_data)
        basic_info.achievements_and_awards.set(AchievementAndAward.objects.create(**item) for item in achievements_and_awards_data)
        basic_info.publications.set(Publication.objects.create(**item) for item in publications_data)
        basic_info.references.set(Reference.objects.create(**item) for item in references_data)

        return basic_info

    def update(self, instance, validated_data):
        industry_knowledge_data = validated_data.pop('industry_knowledge', [])
        tools_data = validated_data.pop('tools', [])
        other_skills_data = validated_data.pop('other_skills', [])
        languages_data = validated_data.pop('languages', [])
        educations_data = validated_data.pop('educations', [])
        experiences_data = validated_data.pop('experiences', [])
        projects_data = validated_data.pop('projects', [])
        interests_data = validated_data.pop('interests', [])
        activities_data = validated_data.pop('activities', [])
        achievements_and_awards_data = validated_data.pop('achievements_and_awards', [])
        publications_data = validated_data.pop('publications', [])
        references_data = validated_data.pop('references', [])

        instance = super(BasicInformationSerializer, self).update(instance, validated_data)

        # Update and associate related objects
        instance.industry_knowledge.set(IndustryKnowledge.objects.create(**item) for item in industry_knowledge_data)
        instance.tools.set(Tool.objects.create(**item) for item in tools_data)
        instance.other_skills.set(OtherSkill.objects.create(**item) for item in other_skills_data)
        instance.languages.set(Language.objects.create(**item) for item in languages_data)
        instance.educations.set(Education.objects.create(**item) for item in educations_data)
        instance.experiences.set(Experience.objects.create(**item) for item in experiences_data)
        instance.projects.set(Project.objects.create(**item) for item in projects_data)
        instance.interests.set(Interest.objects.create(**item) for item in interests_data)
        instance.activities.set(Activity.objects.create(**item) for item in activities_data)
        instance.achievements_and_awards.set(AchievementAndAward.objects.create(**item) for item in achievements_and_awards_data)
        instance.publications.set(Publication.objects.create(**item) for item in publications_data)
        instance.references.set(Reference.objects.create(**item) for item in references_data)

        return instance
