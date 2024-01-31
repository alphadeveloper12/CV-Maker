# api/serializers.py

from rest_framework import serializers
from .models import BasicInformation, Experience, Education, IndustryKnowledge, Tool, OtherSkill, Language, Social

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

class BasicInformationSerializer(serializers.ModelSerializer):
    social = SocialSerializer()
    languages = LanguageSerializer(many=True)
    other_skills = OtherSkillSerializer(many=True)
    tools = ToolSerializer(many=True)
    industry_knowledge = IndustryKnowledgeSerializer(many=True)
    educations = EducationSerializer(many=True)
    experiences = ExperienceSerializer(many=True)

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

        basic_info = BasicInformation.objects.create(**validated_data)

        # Create and associate related objects
        basic_info.industry_knowledge.set(IndustryKnowledge.objects.create(**item) for item in industry_knowledge_data)
        basic_info.tools.set(Tool.objects.create(**item) for item in tools_data)
        basic_info.other_skills.set(OtherSkill.objects.create(**item) for item in other_skills_data)
        basic_info.languages.set(Language.objects.create(**item) for item in languages_data)
        basic_info.educations.set(Education.objects.create(**item) for item in educations_data)
        basic_info.experiences.set(Experience.objects.create(**item) for item in experiences_data)

        return basic_info

    def update(self, instance, validated_data):
        industry_knowledge_data = validated_data.pop('industry_knowledge', [])
        tools_data = validated_data.pop('tools', [])
        other_skills_data = validated_data.pop('other_skills', [])
        languages_data = validated_data.pop('languages', [])
        educations_data = validated_data.pop('educations', [])
        experiences_data = validated_data.pop('experiences', [])

        instance = super(BasicInformationSerializer, self).update(instance, validated_data)

        # Update and associate related objects
        instance.industry_knowledge.set(IndustryKnowledge.objects.create(**item) for item in industry_knowledge_data)
        instance.tools.set(Tool.objects.create(**item) for item in tools_data)
        instance.other_skills.set(OtherSkill.objects.create(**item) for item in other_skills_data)
        instance.languages.set(Language.objects.create(**item) for item in languages_data)
        instance.educations.set(Education.objects.create(**item) for item in educations_data)
        instance.experiences.set(Experience.objects.create(**item) for item in experiences_data)

        return instance
