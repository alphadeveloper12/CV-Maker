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


def cv_detail(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template1.html', context={'cv': cv})


def cv_list(request):
    cvs = BasicInformation.objects.all()
    return render(request, 'index.html', {'cvs': cvs})


class CVDetailView(View):
    def get(self, request, cv_id):
        cv = BasicInformation.objects.get(pk=cv_id)
        template = get_template('template1.html')
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
        pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[CSS(string='@page { size: A4;margin: 0; }')])

        # Create an HTTP response with the PDF content
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={cv.last_name}_cv.pdf'

        return response
