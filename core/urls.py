from django.urls import path
from . import views

from .views import (Barcodeinlistview, Barcodedeleteview, BarcodeGenerateView)
from .views import (codeinlistview, codedeleteview, codeGenerateView)

urlpatterns = [
    path('', views.index, name='index'),
    path('Barcodeindata/', Barcodeinlistview.as_view(), name='Barcodeinlistview'),
    path('Barcodedata/<int:pk>/', Barcodedeleteview.as_view(), name='Barcodedeleteview'),
    path('gene/', BarcodeGenerateView.as_view(), name='BarcodeGenerateView'),


    path('codeindata/', codeinlistview.as_view(), name='codeinlistview'),
    path('codedata/<int:pk>/', codedeleteview.as_view(), name='codedeleteview'),
    path('data/', codeGenerateView.as_view(), name='codeGenerateView'),
]

