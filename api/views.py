# api/views.py
import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BasicInformationSerializer
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from weasyprint import HTML, CSS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from api.models import BasicInformation
from django.shortcuts import render, redirect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Template
from .serializers import TemplateSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class TemplateListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        templates = Template.objects.filter(is_active=True)
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

class AddDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user_id = request.data.get('user', None)
        if user_id is not None:
            # Check if BasicInformation already exists for the user
            try:
                basic_info = BasicInformation.objects.get(user_id=user_id)
                serializer = BasicInformationSerializer(basic_info, data=request.data)
            except BasicInformation.DoesNotExist:
                serializer = BasicInformationSerializer(data=request.data)

            if serializer.is_valid():
                basic_info = serializer.save()
                cv = BasicInformation.objects.get(pk=basic_info.id)
                template_id = cv.template.base
                template_full_url = os.path.join(settings.BASE_DIR, template_id)
                template = get_template(template_full_url)
                context = {'cv': cv}
                html_content = template.render(context)
                # Use Selenium to render the template
                chrome_options = Options()
                chrome_options.add_argument('--headless')  # Run in headless mode (without GUI)

                with webdriver.Chrome(options=chrome_options) as driver:
                    driver.get("about:blank")
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'body'))
                    )
                    driver.execute_script(f"document.write(`{html_content}`);")

                    # Get the HTML content after rendering with JavaScript
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'body'))
                    )

                    # Get the HTML content after rendering with JavaScript
                    rendered_html = driver.page_source

                # Generate PDF using WeasyPrint with a large width
                pdf_file = HTML(string=rendered_html).write_pdf(
                    stylesheets=[CSS(string='@page { size: A4;margin: 0; }')])

                # Create an HTTP response with the PDF content
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename={cv.last_name}_cv.pdf'

                return response
                # return Response({'basic_information_id': basic_info.id}, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response({'error': f'Invalid Params Sent {serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid or missing user ID'}, status=status.HTTP_400_BAD_REQUEST)


class CVPdf(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request, format=None):
        user_id = request.data.get('user', None)
        request_body = request.data.copy()
        if user_id is not None:
            try:
                basic_info = BasicInformation.objects.get(user_id=user_id)
                serializer = BasicInformationSerializer(basic_info, data=request.data)
            except BasicInformation.DoesNotExist:
                serializer = BasicInformationSerializer(data=request.data)

            if serializer.is_valid():
                basic_info = serializer.save()
                cv = BasicInformation.objects.get(pk=basic_info.id)
                template_id = cv.template.base
                template_full_url = os.path.join(settings.BASE_DIR, template_id)
                template = get_template(template_full_url)
                context = {'cv': cv}
                html_content = template.render(context)

                chrome_options = Options()
                chrome_options.add_argument('--headless')

                with webdriver.Chrome(options=chrome_options) as driver:
                    driver.get("about:blank")
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'body'))
                    )
                    driver.execute_script(f"document.write(`{html_content}`);")
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'body'))
                    )
                    rendered_html = driver.page_source

                # Generate PDF using WeasyPrint
                pdf_file = HTML(string=rendered_html).write_pdf(
                    stylesheets=[CSS(string='@page { size: A4;margin: 0; }')])

                # Save the PDF to the media folder
                media_folder = settings.MEDIA_ROOT
                unique_id = uuid.uuid4()
                filename = f'{cv.last_name}_cv_{unique_id}.pdf'
                pdf_path = os.path.join(media_folder, filename)

                with default_storage.open(pdf_path, 'wb') as pdf_file_handle:
                    pdf_file_handle.write(pdf_file)

                # Create an HTTP response with the PDF content
                response = HttpResponse(pdf_file, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename={cv.last_name}_cv.pdf'

                # Return the file path in the API response
                return Response({'pdf_link': f'/media/{filename}', 'data': request_body}, status=status.HTTP_200_OK)
            else:
                print(serializer.errors)
                return Response({'error': f'Invalid Params Sent {serializer.errors}'},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid or missing user ID'}, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'user': serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)


        return Response({
            'user': UserSerializer(user).data
        }, status=status.HTTP_200_OK)

# class UpdateBasicInformationView(APIView):
#     def put(self, request, format=None):
#         temp_id = request.data.get('template', None)
#
#         if temp_id is None:
#             return Response({'error': 'temp_id is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             basic_info = BasicInformation.objects.get(template__id=temp_id)
#         except BasicInformation.DoesNotExist:
#             return Response({'error': 'BasicInformation not found for the given template id'},
#                             status=status.HTTP_404_NOT_FOUND)
#
#         serializer = BasicInformationSerializer(basic_info, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserTemplatesView(APIView):
#     def post(self, request, format=None):
#         try:
#             user_id = request.data.get('user_id')
#             user_templates = BasicInformation.objects.filter(user_id=user_id).values_list('template', flat=True)
#             templates = Template.objects.filter(id__in=user_templates)
#             serializer = TemplateSerializer(templates, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
