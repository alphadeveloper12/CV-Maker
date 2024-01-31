# api/views.py

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

class AddDataView(APIView):
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
                template = get_template('/home/alphadeveloper/PycharmProjects/CV/web/templates/template1.html')
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

        return Response({'error': 'Invalid or missing user ID'}, status=status.HTTP_400_BAD_REQUEST)

