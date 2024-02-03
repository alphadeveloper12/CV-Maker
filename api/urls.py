
from django.urls import path
from .views import *

urlpatterns = [
    path('add-data/', AddDataView.as_view(), name='add_data'),
    path('templates/', TemplateListView.as_view(), name='template_list'),
    path('cv-pdf/', CVPdf.as_view(), name='cv_pdf'),
    # path('update_basic_info/', UpdateBasicInformationView.as_view(), name='update_basic_info'),
    # path('user_templates/', UserTemplatesView.as_view(), name='user_templates'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
