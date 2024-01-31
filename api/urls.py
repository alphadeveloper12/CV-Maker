
from django.urls import path
from .views import AddDataView

urlpatterns = [
    path('add-data/', AddDataView.as_view(), name='add_data'),
]