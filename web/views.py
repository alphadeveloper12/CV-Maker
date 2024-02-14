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
from django.conf import settings
from django.http import HttpResponseBadRequest
import os

def cv_detail_1(request, cv_id):
    try:
        cv = BasicInformation.objects.get(pk=cv_id)
        image = cv.image.url  # Assuming cv.image is a FileField or ImageField
    except BasicInformation.DoesNotExist:
        return HttpResponseBadRequest("CV not found")

    # Build the absolute URL by combining the base URL and the media URL
    absolute_url = request.build_absolute_uri(image)
    print(absolute_url)

    # Include the absolute_url in the context
    context = {'cv': cv, 'absolute_url': absolute_url}

    return render(request, 'template1.html', context=context)


def cv_detail_2(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template2.html', context={'cv': cv})


def cv_detail_3(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template3.html', context={'cv': cv})


def cv_detail_4(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template4.html', context={'cv': cv})

def cv_detail_5(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    image = cv.image.url
    absolute_url = request.build_absolute_uri(image)
    template_id = cv.template.base
    template_full_url = os.path.join(settings.BASE_DIR, template_id)
    template = get_template(template_full_url)
    context = {'cv': cv, 'absolute_url': absolute_url}
    return render(request, 'template5.html', context=context)

def cv_detail_6(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template6.html', context={'cv': cv})

def cv_detail_7(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    image = cv.image.url
    absolute_url = request.build_absolute_uri(image)
    template_id = cv.template.base
    template_full_url = os.path.join(settings.BASE_DIR, template_id)
    template = get_template(template_full_url)
    context = {'cv': cv, 'absolute_url': absolute_url}
    return render(request, 'template7.html', context=context)

def cv_detail_8(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    image = cv.image.url
    absolute_url = request.build_absolute_uri(image)
    template_id = cv.template.base
    template_full_url = os.path.join(settings.BASE_DIR, template_id)
    template = get_template(template_full_url)
    context = {'cv': cv, 'absolute_url': absolute_url}
    return render(request, 'template8.html', context=context)

def cv_detail_9(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template9.html', context={'cv': cv})

def cv_detail_10(request, cv_id):
    cv = BasicInformation.objects.get(pk=cv_id)
    return render(request, 'template10.html', context={'cv': cv})

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
